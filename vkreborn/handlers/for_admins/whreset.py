from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.repositories import WHPictureRepository
from vkreborn.error_handler import error_handler


@labeler.chat_message(text="<_:prefix>whreset", admin=True)
@error_handler.catch
async def giveadmin_handler(message: Message):
    repo = WHPictureRepository(where_id=message.chat_id)
    await repo.reset_chat()
    return await message.reply("Кэш комманды wh очищен")
