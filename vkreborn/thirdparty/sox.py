from subprocess import check_output
from vkreborn.config import FX_NIGHTCORE_SPEED, FX_DAYCORE_SPEED


FILTERS = {"speed": "speed {}", "reverb": "reverb {}", "reverb_def": "reverb 80"}
FILTERS["nightcore"] = FILTERS["speed"].replace("{}", str(FX_NIGHTCORE_SPEED), 1)
FILTERS["daycore"] = FILTERS["speed"].replace("{}", str(FX_DAYCORE_SPEED), 1)

FILTER_NAME_FUNCS = {
    "speed": lambda speed: f"daycore x{speed}"
    if speed <= FX_DAYCORE_SPEED
    else f"nightcore x{speed}",
    "nightcore": lambda _: "nightcore",
    "daycore": lambda _: "daycore",
    "reverb": lambda p: f"reverb {p}%",
    "reverb_def": lambda _: "reverb",
}


async def apply_fx(content: bytes, **fx: dict):
    filters = await generate_filters(fx)
    return check_output(
        ["sox", "-G", "-t", "mp3", "-", "-t", "mp3", "-"] + filters, input=content
    )


async def make_title(title: str, **fx: dict):
    filters = [FILTER_NAME_FUNCS[name](value) for name, value in fx.items()]
    return f"{title} +| {', '.join(filters)}"


async def generate_filters(fx: dict, **kwargs):
    filters = [FILTERS[name].format(value, **kwargs) for name, value in fx.items()]
    return " ".join(filters).split(" ")
