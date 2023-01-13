from vbml import Patcher
import shlex
import re

patcher = Patcher()


@patcher.validator("list")
def list_validator(value: str):
    return shlex.split(value, posix=True)


@patcher.validator("mention")
def mention_validator(value: str):
    pattern = re.compile(r"^\[id[0-9]+\|@[A-Za-z0-9]+]$", re.IGNORECASE)
    if pattern.match(value):
        value = value.split("|")
        return {
            "id": int(value[0].removeprefix("[id")),
            "domain": value[1].removesuffix("]"),
        }


@patcher.validator("prefix")
def prefix_validator(value: str):
    if value == "%!":
        return True


@patcher.validator("wh-switches")
def wh_switches_validator(value: str):
    if len(value) not in [3, 6]:  # "000" or "0 0 0"
        return

    if " " in value:
        value = value.replace(" ", "")

    for numba in value:
        if not numba.isdigit():
            return

    return value
