from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import WHPictureRepository
from vkreborn.vkbottle import labeler


@labeler.chat_message(text="<_:prefix>whgreset", owner=True)
@labeler.chat_message(text="<_:prefix>wallhavengreset", owner=True)
@labeler.chat_message(text="<_:prefix>wallhavenglobalreset", owner=True)
@labeler.chat_message(text="<_:prefix>вхгрезет", owner=True)
@labeler.chat_message(text="<_:prefix>валлхавенгрезет", owner=True)
@labeler.chat_message(text="<_:prefix>воллхавенгрезет", owner=True)
@labeler.chat_message(text="<_:prefix>валхавенгрезет", owner=True)
@labeler.chat_message(text="<_:prefix>волхавенгрезет", owner=True)
@labeler.chat_message(text="<_:prefix>валлхавэнгрезет", owner=True)
@labeler.chat_message(text="<_:prefix>воллхавэнгрезет", owner=True)
@labeler.chat_message(text="<_:prefix>валхавэнгрезет", owner=True)
@labeler.chat_message(text="<_:prefix>волхавэнгрезет", owner=True)
@labeler.chat_message(text="<_:prefix>валлхавнгрезет", owner=True)
@labeler.chat_message(text="<_:prefix>воллхавнгрезет", owner=True)
@labeler.chat_message(text="<_:prefix>валхавнгрезет", owner=True)
@labeler.chat_message(text="<_:prefix>волхавнгрезет", owner=True)
@labeler.chat_message(text="<_:prefix>вхгресет", owner=True)
@labeler.chat_message(text="<_:prefix>валлхавенгресет", owner=True)
@labeler.chat_message(text="<_:prefix>воллхавенгресет", owner=True)
@labeler.chat_message(text="<_:prefix>валхавенгресет", owner=True)
@labeler.chat_message(text="<_:prefix>волхавенгресет", owner=True)
@labeler.chat_message(text="<_:prefix>валлхавэнгресет", owner=True)
@labeler.chat_message(text="<_:prefix>воллхавэнгресет", owner=True)
@labeler.chat_message(text="<_:prefix>валхавэнгресет", owner=True)
@labeler.chat_message(text="<_:prefix>волхавэнгресет", owner=True)
@labeler.chat_message(text="<_:prefix>валлхавнгресет", owner=True)
@labeler.chat_message(text="<_:prefix>воллхавнгресет", owner=True)
@labeler.chat_message(text="<_:prefix>валхавнгресет", owner=True)
@labeler.chat_message(text="<_:prefix>волхавнгресет", owner=True)
@error_handler.catch
async def whgreset_handler(message: Message):
    repo = WHPictureRepository()
    await repo.reset_all()
    return await message.reply("Кэш комманды wh очищен глобально")
