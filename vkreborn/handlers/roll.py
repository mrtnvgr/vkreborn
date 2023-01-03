from vkbottle.user import Message, UserLabeler
from vkbottle.dispatch.rules.base import VBMLRule
from vbml import Patcher
import shlex
import random

patcher = Patcher()


@patcher.validator("list")
def list_validator(value: str):
    return shlex.split(value, posix=True)


labeler = UserLabeler()


@labeler.message(command="roll")
async def roll_default_handler(message: Message):
    response = random.randint(1, 100)
    return await message.reply(response)


@labeler.message(text="<_>roll <start:int>-<end:int>")
async def roll_ints_handler(message: Message, start: int, end: int):
    response = random.randint(start, end)
    return await message.reply(response)


@labeler.message(VBMLRule("<_>roll <args:list>", patcher=patcher))
async def roll_strings_handler(message: Message, args: list):
    choice = random.choice(args)
    return await message.reply(cleanup(choice))


def cleanup(value: str):
    value = value.removesuffix(",")
    return value
