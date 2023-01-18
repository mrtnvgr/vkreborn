from tempfile import NamedTemporaryFile
from subprocess import check_output, run, DEVNULL
import json
import os


FILTERS = {"speed": "asetrate={}*{sample_rate}"}
FILTER_NAME_FUNCS = {"speed": lambda speed: "nightcore" if speed > 1 else "daycore"}


async def apply_fx(content: bytes, **fx: dict):

    with NamedTemporaryFile(suffix=".mp3") as source_file:

        source_file.seek(0)

        source_file.write(content)

        output = os.path.join(
            os.path.dirname(source_file.name),
            "out_" + os.path.basename(source_file.name),
        )

        sample_rate = await get_sample_rate(source_file.name)

        filters = await generate_filters(fx, sample_rate=sample_rate)

        run(
            [
                "ffmpeg",
                "-i",
                source_file.name,
                "-ab",
                "320k",
                "-filter:a",
                ",".join(filters),
                output,
            ],
            check=False,
            stdout=DEVNULL,
            stderr=DEVNULL,
        )

        with open(output, "rb") as f:
            data = f.read()

    os.remove(output)

    return data


async def make_title(title: str, **fx: dict):
    filters = [FILTER_NAME_FUNCS[name](value) for name, value in fx.items()]
    return f"{title} +| {', '.join(filters)}"


async def generate_filters(fx: dict, **kwargs):
    return [FILTERS[name].format(value, **kwargs) for name, value in fx.items()]


async def get_sample_rate(file: str):
    payload = [
        "ffprobe",
        "-hide_banner",
        "-loglevel",
        "panic",
        "-show_streams",
        "-of",
        "json",
        file,
    ]
    info = json.loads(check_output(payload))
    return info["streams"][0]["sample_rate"]
