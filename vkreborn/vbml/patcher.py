import re
import shlex

from vbml import Patcher

ABS_FLOAT_RE = r"(?:\d+?)(?:[\.\,]?\d*)"

TT_URL_RE = r"""
(?x)
^
    https?://
    (?:
       (?:www|m)\.
       (?:tiktok.com)\/
       (?:v|embed|trending|h5/share/usr/|share/user/|@[a-zA-Z]*/video)
       (?:\/)?
       (?:\?shareId=)?
    )
    (?P<id>[\da-z]+)
$
"""

PERCENTAGE_RE = r"""
(?x)
^
    (?:
        (?:^(?!-))
        (?:[+]?)
    )
    (?P<pt>\d*[\,\.]?\d*)
    (?:[%]?)
$
"""

patcher = Patcher()


@patcher.validator("list")
def list_validator(value: str):
    return shlex.split(value, posix=True)


@patcher.validator("mention")
def mention_validator(value: str):
    pattern = re.compile(r"^\[id([0-9]+)\|@([A-Za-z0-9]+)]$", re.IGNORECASE)
    match = pattern.match(value)
    return (
        {"id": int(match.groups()[0]), "domain": match.groups()[1]} if match else None
    )


@patcher.validator("prefix")
def prefix_validator(value: str):
    return True if value == "%!" else None


@patcher.validator("wh_switches")
def wh_switches_validator(value: str):
    pattern = re.compile(r"^[01]{3}$", re.IGNORECASE)
    return value if pattern.match(value) else None


@patcher.validator("abs_float")
def custom_abs_float_validator(value: str):
    pattern = re.compile(f"^{ABS_FLOAT_RE}$", re.IGNORECASE)
    return str_to_float(value) if pattern.match(value) else None


@patcher.validator("float")
def custom_float_validator(value: str):
    pattern = re.compile(f"^[+-]?{ABS_FLOAT_RE}$", re.IGNORECASE)
    return str_to_float(value) if pattern.match(value) else None


@patcher.validator("percentage")
def percentage_validator(value: str):
    pattern = re.compile(PERCENTAGE_RE, re.IGNORECASE)
    match = pattern.match(value)
    if not match:
        return
    value = str_to_float(match.groups()[0])

    if value > 100:
        return 100
    elif value < 0:
        return 0

    return value


@patcher.validator("gain")
def gain_validator(value: str):
    pattern = re.compile(f"^[+-]?{ABS_FLOAT_RE}(db)?$", re.IGNROECASE)
    return value if pattern.match(value) else None


@patcher.validator("tt_url")
def tt_url_validator(value: str):
    pattern = re.compile(TT_URL_RE)
    return value if pattern.match(value) else None


def str_to_float(value: str):
    return float(value.replace(",", "."))
