import os
from subprocess import check_output

from aiofiles.tempfile import NamedTemporaryFile


async def mix_audios(audios: list[bytes]):
    files = []
    for audio in audios:
        async with NamedTemporaryFile("wb", suffix=".mp3", delete=False) as file:
            await file.write(audio)
            files.append(file)

    file_names = [file.name for file in files]

    payload = ["sox", "-m", *file_names, "-t", "mp3", "-"]

    output = check_output(payload)

    for file_name in file_names:
        if os.path.exists(file_name):
            os.remove(file_name)

    return output
