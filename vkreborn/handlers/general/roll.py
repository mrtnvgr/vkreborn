import random

from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = ["roll", "rol", "ролл", "рол"]


@labeler.message(AliasRule(ALIASES))
@error_handler.catch
async def roll_default_handler(message: Message):
    await randint(message, 1, 100)


@labeler.message(AliasRule(ALIASES, "<start:int>-<end:int>"))
@error_handler.catch
async def roll_ints_handler(message: Message, start: int, end: int):
    await randint(message, start, end)


@labeler.message(AliasRule(ALIASES, "<args:list>"))
@error_handler.catch
async def roll_strings_handler(message: Message, args: list):
    choice = random.choice(args)
    return await message.reply(wrap(cleanup(choice)))


wrap = lambda text: f'Результат: "{text}"'


async def randint(message: Message, start: int, end: int):
    try:
        response = random.randint(start, end)
        await message.reply(wrap(response))
    except ValueError:
        await message.reply(
            "Ошибка. Конечное число меньше начального."
            "\n(Если вы хотели выбрать одно из чисел, a не из диапазона, то "
            f'попробуйте "{start}, {end}", а не "{start}-{end}".)'
        )


def cleanup(value: str):
    value = value.removesuffix(",")
    return value
