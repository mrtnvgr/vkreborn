from typing import Optional

from async_google_trans_new import AsyncTranslator, TransError
from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = ["trans", "транс", "translate", "перевод", "перевести", "translator", "переводчик"]
DEFAULT_TO_ARG = "ru"


@labeler.message(AliasRule(ALIASES), reply=True)
@error_handler.catch
async def trans_handler(message: Message):
    content = message.reply_message.text
    response = await translate(content)
    return await message.reply(response)


@labeler.message(AliasRule(ALIASES, "<to>"), reply=True)
@error_handler.catch
async def trans_to_handler(message: Message, to: str):
    content = message.reply_message.text
    response = await translate(content, to=to)
    return await message.reply(response)


async def translate(content: str, to: Optional[str] = None):
    try:
        to = expand_to_arg(to)
        translator = AsyncTranslator()
        response = await translator.translate(text=content, lang_tgt=to)
    except TransError as ex:
        return f"Произошла неожиданная ошибка!\n{ex.status_code}: {ex.reason}"

    return f'Перевод: "{response.strip()}"'


def expand_to_arg(to: Optional[str] = None):
    if not to:
        return DEFAULT_TO_ARG

    to = to.lower()
    to_map = {
        "ru": ("ру", "рус", "русский", "русский язык", "russian", "rus"),
        "en": ("ен", "енг", "ин", "инг", "инглиш", "english", "eng"),
        # TODO: japanesse, de, chinesse, ukranian, ...
        # TODO: mention these custom values in docs
    }
    for key, values in to_map.items():
        if to in values:
            return key
