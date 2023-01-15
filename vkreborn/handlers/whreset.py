from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.repositories import WHPictureRepository
from vkreborn.error_handler import error_handler


@labeler.private_message(text="<_:prefix>whreset")
@error_handler.catch
async def pm_whreset_handler(message: Message):
    repo = WHPictureRepository(where_id=message.chat_id)
    await repo.reset_chat()
    return await message.reply("Кэш комманды wh очищен")