import random

from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.vkbottle import labeler


@labeler.message(text="<_:prefix>roll", blocking=False)
@labeler.message(text="<_:prefix>rol", blocking=False)
@labeler.message(text="<_:prefix>ролл", blocking=False)
@labeler.message(text="<_:prefix>рол", blocking=False)
@error_handler.catch
async def roll_default_handler(message: Message):
    response = random.randint(1, 100)
    return await message.reply(response)


@labeler.message(text="<_:prefix>roll <start:int>-<end:int>", blocking=False)
@labeler.message(text="<_:prefix>rol <start:int>-<end:int>", blocking=False)
@labeler.message(text="<_:prefix>ролл <start:int>-<end:int>", blocking=False)
@labeler.message(text="<_:prefix>рол <start:int>-<end:int>", blocking=False)
@error_handler.catch
async def roll_ints_handler(message: Message, start: int, end: int):
    response = random.randint(start, end)
    return await message.reply(response)


@labeler.message(text="<_:prefix>roll <args:list>", blocking=False)
@labeler.message(text="<_:prefix>rol <args:list>", blocking=False)
@labeler.message(text="<_:prefix>ролл <args:list>", blocking=False)
@labeler.message(text="<_:prefix>рол <args:list>", blocking=False)
@error_handler.catch
async def roll_strings_handler(message: Message, args: list):
    choice = random.choice(args)
    return await message.reply(cleanup(choice))


def cleanup(value: str):
    value = value.removesuffix(",")
    return value
