from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = ["fl", "фл", "fixlayout", "фикслайаут"]


def translate(string: str):
    ru = """ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"""
    en = """`qwertyuiop[]asdfghjkl;'zxcvbnm,./~@#$%^&QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?"""
    if any(i in string and i.isalnum() for i in ru):
        change = string.maketrans(ru, en)
    else:
        change = string.maketrans(en, ru)
    return string.translate(change)


@labeler.message(AliasRule(ALIASES), reply=True)
@error_handler.catch
async def fixlayout_reply_handler(message: Message):
    text = message.reply_message.text
    await message.reply(f'Перевод: "{translate(text)}"')


@labeler.message(AliasRule(ALIASES, "<text>"))
@error_handler.catch
async def fixlayout_handler(message: Message, text: str):
    await message.reply(f'Перевод: "{translate(text)}"')
