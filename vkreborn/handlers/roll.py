from vkbottle.user import Message, UserLabeler
from vkbottle.dispatch.rules.base import CommandRule
import random

labeler = UserLabeler()


@labeler.message(command="roll")
async def roll_default_handler(message: Message):
    response = random.randint(1, 100)
    return await message.reply(response)


@labeler.message(CommandRule("roll", args_count=1), text="<_> <start:int>-<end:int>")
async def roll_ints_handler(message: Message, start: int, end: int):
    response = random.randint(start, end)
    return await message.reply(response)
