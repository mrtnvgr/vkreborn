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


@patcher.validator("wh_switches")
def wh_switches_validator(value: str):
    if len(value) != 3:  # "000"
        return

    for numba in value:
        if numba not in ["0", "1"]:
            return

    return value


@patcher.validator("abs_float")
def custom_abs_float_validator(value: str):
    value = value.replace(",", ".", 1)
    value2 = value.replace(".", "", 1)
    if value2.isdigit():
        return float(value)


@patcher.validator("float")
def custom_float_validator(value: str):
    value2 = value.replace("-", "", 1).replace("+", "", 1)
    if custom_abs_float_validator(value2):
        return float(value)


@patcher.validator("percentage")
def percentage_validator(value: str):
    value = value.removesuffix("%")

    if not value.isdigit():
        return

    value = int(value)

    if value < 0:
        return 0
    elif value > 100:
        return 100
    else:
        return value
