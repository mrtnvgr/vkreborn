from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import WHPictureRepository
from vkreborn.vkbottle import labeler


@labeler.chat_message(text="<_:prefix>whreset", moder=True)
@labeler.chat_message(text="<_:prefix>wallhavenreset", moder=True)
@labeler.chat_message(text="<_:prefix>вхрезет", moder=True)
@labeler.chat_message(text="<_:prefix>валлхавенрезет", moder=True)
@labeler.chat_message(text="<_:prefix>воллхавенрезет", moder=True)
@labeler.chat_message(text="<_:prefix>валхавенрезет", moder=True)
@labeler.chat_message(text="<_:prefix>волхавенрезет", moder=True)
@labeler.chat_message(text="<_:prefix>валлхавэнрезет", moder=True)
@labeler.chat_message(text="<_:prefix>воллхавэнрезет", moder=True)
@labeler.chat_message(text="<_:prefix>валхавэнрезет", moder=True)
@labeler.chat_message(text="<_:prefix>волхавэнрезет", moder=True)
@labeler.chat_message(text="<_:prefix>валлхавнрезет", moder=True)
@labeler.chat_message(text="<_:prefix>воллхавнрезет", moder=True)
@labeler.chat_message(text="<_:prefix>валхавнрезет", moder=True)
@labeler.chat_message(text="<_:prefix>волхавнрезет", moder=True)
@labeler.chat_message(text="<_:prefix>вхресет", moder=True)
@labeler.chat_message(text="<_:prefix>валлхавенресет", moder=True)
@labeler.chat_message(text="<_:prefix>воллхавенресет", moder=True)
@labeler.chat_message(text="<_:prefix>валхавенресет", moder=True)
@labeler.chat_message(text="<_:prefix>волхавенресет", moder=True)
@labeler.chat_message(text="<_:prefix>валлхавэнресет", moder=True)
@labeler.chat_message(text="<_:prefix>воллхавэнресет", moder=True)
@labeler.chat_message(text="<_:prefix>валхавэнресет", moder=True)
@labeler.chat_message(text="<_:prefix>волхавэнресет", moder=True)
@labeler.chat_message(text="<_:prefix>валлхавнресет", moder=True)
@labeler.chat_message(text="<_:prefix>воллхавнресет", moder=True)
@labeler.chat_message(text="<_:prefix>валхавнресет", moder=True)
@labeler.chat_message(text="<_:prefix>волхавнресет", moder=True)
@error_handler.catch
async def whreset_handler(message: Message):
    repo = WHPictureRepository(where_id=message.chat_id)
    await repo.reset_chat()
    return await message.reply("Кэш комманды wh очищен")
