from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import MutedUserRepository
from vkreborn.vkbottle import labeler


@labeler.chat_message(text="<_:prefix>whomuted <user:mention>")
@labeler.chat_message(text="<_:prefix>хумутед <user:mention>")
@labeler.chat_message(text="<_:prefix>хумутэд <user:mention>")
@labeler.chat_message(text="<_:prefix>хумьютед <user:mention>")
@labeler.chat_message(text="<_:prefix>хумьютэд <user:mention>")
@labeler.chat_message(text="<_:prefix>вхумутед <user:mention>")
@labeler.chat_message(text="<_:prefix>вхумутэд <user:mention>")
@labeler.chat_message(text="<_:prefix>вхумьютед <user:mention>")
@labeler.chat_message(text="<_:prefix>вхумьютэд <user:mention>")
@error_handler.catch
async def whomuted_handler(message: Message, user: dict):
    repo = MutedUserRepository(user_id=user["id"], muted_where=message.chat_id)
    user_info = await repo.get()

    if not user_info:
        return await message.reply(f"Пользователь {user['domain']} не замьючен")

    moder = (await message.ctx_api.users.get(user_info.muted_by, fields=["domain"]))[0]
    moder_info = f"{moder.first_name} {moder.last_name} ({moder.domain})"
    return await message.reply(f"Пользователя {user['domain']} замьютил:\n{moder_info}")
