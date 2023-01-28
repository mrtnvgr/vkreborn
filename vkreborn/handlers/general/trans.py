from async_google_trans_new import AsyncTranslator, TransError
from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.vkbottle import labeler


@labeler.message(text="<_:prefix>trans", reply=True, blocking=False)
@labeler.message(text="<_:prefix>транс", reply=True, blocking=False)
@labeler.message(text="<_:prefix>translate", reply=True, blocking=False)
@labeler.message(text="<_:prefix>перевод", reply=True, blocking=False)
@labeler.message(text="<_:prefix>перевести", reply=True, blocking=False)
@labeler.message(text="<_:prefix>translator", reply=True, blocking=False)
@labeler.message(text="<_:prefix>переводчик", reply=True, blocking=False)
@error_handler.catch
async def trans_handler(message: Message):
    content = message.reply_message.text
    response = await translate(content)
    return await message.reply(response)


@labeler.message(text="<_:prefix>trans <to>", reply=True, blocking=False)
@labeler.message(text="<_:prefix>транс <to>", reply=True, blocking=False)
@labeler.message(text="<_:prefix>translate <to>", reply=True, blocking=False)
@labeler.message(text="<_:prefix>перевод <to>", reply=True, blocking=False)
@labeler.message(text="<_:prefix>перевести <to>", reply=True, blocking=False)
@labeler.message(text="<_:prefix>translator <to>", reply=True, blocking=False)
@labeler.message(text="<_:prefix>переводчик <to>", reply=True, blocking=False)
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
