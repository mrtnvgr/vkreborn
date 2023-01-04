from vkbottle.user import Message
from vkbottle.dispatch.rules.base import ReplyMessageRule
from vkreborn.vkbottle import labeler

dictionary = {
    "`": "ё",
    "~": "Ё",
    "@": '"',
    "#": "№",
    "$": ";",
    "^": ":",
    "&": "?",
    "q": "й",
    "w": "ц",
    "e": "у",
    "r": "к",
    "t": "е",
    "y": "н",
    "u": "г",
    "i": "ш",
    "o": "щ",
    "p": "з",
    "х": "[",
    "Х": "{",
    "]": "ъ",
    "}": "Ъ",
    "\\": "/",
    "a": "ф",
    "s": "ы",
    "d": "в",
    "f": "а",
    "g": "п",
    "h": "р",
    "j": "о",
    "k": "л",
    "l": "д",
    ";": "ж",
    ":": "Ж",
    "'": "э",
    '"': "Э",
    "z": "я",
    "x": "ч",
    "c": "с",
    "v": "м",
    "b": "и",
    "n": "т",
    "m": "ь",
    ",": "б",
    "<": "Б",
    ".": "ю",
    ">": "Ю",
    "/": ".",
    "?": ",",
}


def translate(string: str):
    return "".join(
        dictionary.get(ch) or dictionary.get(ch.lower(), "").upper() or ch
        for ch in string
    )


@labeler.message(ReplyMessageRule(), text="<_:prefix>fixlayout")
async def fixlayout_handler(message: Message):
    text = message.reply_message.text
    await message.reply(f'"{translate(text)}"')
