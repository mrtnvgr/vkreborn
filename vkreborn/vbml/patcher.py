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
    if value == "%":
        return True
