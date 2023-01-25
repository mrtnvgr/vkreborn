from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import WHPictureRepository
from vkreborn.vkbottle import labeler


@labeler.chat_message(text="<_:prefix>whreset", moder=True)
@error_handler.catch
async def whreset_handler(message: Message):
    repo = WHPictureRepository(where_id=message.chat_id)
    await repo.reset_chat()
    return await message.reply("Кэш комманды wh очищен")
