import random

from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = ["roll", "rol", "ролл", "рол"]


@labeler.message(AliasRule(ALIASES))
@error_handler.catch
async def roll_default_handler(message: Message):
    response = random.randint(1, 100)
    return await message.reply(wrap(response))


@labeler.message(AliasRule(ALIASES, "<start:int>-<end:int>"))
@error_handler.catch
async def roll_ints_handler(message: Message, start: int, end: int):
    response = random.randint(start, end)
    return await message.reply(wrap(response))


@labeler.message(AliasRule(ALIASES, "<args:list>"))
@error_handler.catch
async def roll_strings_handler(message: Message, args: list):
    choice = random.choice(args)
    return await message.reply(wrap(cleanup(choice)))


wrap = lambda text: f'Результат: "{text}"'


def cleanup(value: str):
    value = value.removesuffix(",")
    return value
