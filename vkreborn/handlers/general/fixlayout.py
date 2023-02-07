from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler


def translate(string: str):
    ru = """ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"""
    en = """`qwertyuiop[]asdfghjkl;'zxcvbnm,./~@#$%^&QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?"""
    if any(i in string for i in ru):
        change = string.maketrans(ru, en)
    else:
        change = string.maketrans(en, ru)
    return string.translate(change)


@labeler.message(AliasRule(["fl", "фл", "fixlayout", "фикслайаут"]), reply=True)
@error_handler.catch
async def fixlayout_handler(message: Message):
    text = message.reply_message.text
    await message.reply(f'Перевод: "{translate(text)}"')
