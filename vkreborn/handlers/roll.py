from vkbottle.user import Message
from vkreborn.vkbottle import labeler
import random


@labeler.message(command="roll")
async def roll_default_handler(message: Message):
    response = random.randint(1, 100)
    return await message.reply(response)


@labeler.message(text="<_>roll <start:int>-<end:int>")
async def roll_ints_handler(message: Message, start: int, end: int):
    response = random.randint(start, end)
    return await message.reply(response)


@labeler.message(text="<_>roll <args:list>")
async def roll_strings_handler(message: Message, args: list):
    choice = random.choice(args)
    return await message.reply(cleanup(choice))


def cleanup(value: str):
    value = value.removesuffix(",")
    return value
