import re
import shlex

from vbml import Patcher

patcher = Patcher()

TT_URL_RE = r"(https?:\/\/)?(www|m)(\.tiktok\.com)(\/.*\/|\/trending.?shareId=)([\d]*)(\.html)?"


@patcher.validator("list")
def list_validator(value: str):
    return [item.removesuffix(",") for item in shlex.split(value, posix=True)]


@patcher.validator("mention")
def mention_validator(value: str):
    pattern = re.compile(r"^\[id([0-9]+)\|(@[A-Za-z0-9]+)]$")
    match = pattern.match(value)
    return {"id": int(match.groups()[0]), "domain": match.groups()[1]} if match else None


@patcher.validator("prefix")
def prefix_validator(value: str):
    pattern = re.compile(r"^(%!|%)$")
    return value if pattern.match(value) else None


@patcher.validator("wh_switches")
def wh_switches_validator(value: str):
    pattern = re.compile(r"^[01]{3}$")
    return value if pattern.match(value) else None


@patcher.validator("float")
def custom_float_validator(value: str):
    pattern = re.compile(r"^[+-]?\d+?[\.\,]?\d*$")
    return str_to_float(value) if pattern.match(value) else None


@patcher.validator("gain")
def gain_validator(value: str):
    pattern = re.compile(r"(?:\+)?(-?\d+?[\.\,]?\d*)(?:db)?")
    match = pattern.match(value)
    return str_to_float(match.groups()[0]) if match else None


@patcher.validator("tt_url")
def tt_url_validator(value: str):
    pattern = re.compile(f"^{TT_URL_RE}$", re.IGNORECASE)
    return value if pattern.match(value) else None


@patcher.validator("factor")
def factor_validator(value: str):
    percentage = _percentage_validator(value)
    abs_float = _custom_abs_float_validator(value)
    return percentage or abs_float


def _percentage_validator(value: str):
    pattern = re.compile(r"^(?:[+]?)(\d*[\,\.]?\d*)(?:[%]?)$")
    match = pattern.match(value)
    if not match:
        return
    value = str_to_float(match.groups()[0])

    if value > 100:
        return 100
    elif value < 0:
        return 0

    return value


def _custom_abs_float_validator(value: str):
    pattern = re.compile(r"^(x)?\d+?[\.\,]?\d*$")
    return str_to_float(value) if pattern.match(value) else None


def str_to_float(value: str):
    return float(value.replace(",", "."))


@patcher.validator("url")
def url_validator(value: str):
    pattern = re.compile(r"^(?:https?://)?(?:[\w]+\.)(?:\.?[\w]{2,})+(?:/)?$", re.IGNORECASE)
    return value if pattern.match(value) else None


@patcher.validator("literally_str")
def literally_str(value: str):
    return value if len(shlex.split(value, posix=True)) == 1 else None
