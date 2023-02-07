from async_google_trans_new import AsyncTranslator, TransError
from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = ["trans", "транс", "translate", "перевод", "перевести", "translator", "переводчик"]


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


async def translate(content: str, to: str = "ru"):
    try:
        translator = AsyncTranslator()
        response = await translator.translate(text=content, lang_tgt=to)
    except TransError as ex:
        return f"Произошла неожиданная ошибка!\n{ex.status_code}: {ex.reason}"

    return f'Перевод: "{response.strip()}"'
