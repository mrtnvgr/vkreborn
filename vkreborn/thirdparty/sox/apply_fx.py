from subprocess import check_output
from vkreborn.thirdparty.sox.effects import BaseEffect


async def apply_fx(content: bytes, *effects: list[BaseEffect]):
    filters = [effect.filter for effect in effects]
    filters = " ".join(filters).split(" ")
    return check_output(
        ["sox", "-G", "-t", "mp3", "-", "-t", "mp3", "-"] + filters, input=content
    )
