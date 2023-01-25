from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import WHPictureRepository
from vkreborn.vkbottle import labeler


@labeler.chat_message(text="<_:prefix>whgreset", owner=True)
@error_handler.catch
async def whgreset_handler(message: Message):
    repo = WHPictureRepository()
    await repo.reset_all()
    return await message.reply("Кэш комманды wh очищен глобально")
