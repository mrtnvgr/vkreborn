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
            "domain": value[1].removesuffix("]").removeprefix("@"),
        }


@patcher.validator("prefix")
def prefix_validator(value: str):
    if value == "%!":
        return True


@patcher.validator("wh_switches")
def wh_switches_validator(value: str):
    if len(value) != 3:  # "000"
        return

    for numba in value:
        if numba not in ["0", "1"]:
            return

    return value


@patcher.validator("float")
def custom_float_validator(value: str):
    value = value.replace(",", "").replace(".", "")
    if value.isdigit():
        return int(value)
