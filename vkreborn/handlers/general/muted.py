from datetime import datetime

from loguru import logger
from vkbottle.exception_factory import VKAPIError
from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import MutedUserRepository
from vkreborn.vkbottle import labeler


@labeler.chat_message(muted=True)
@error_handler.catch
async def muted_user_handler(message: Message):
    repo = MutedUserRepository(user_id=message.from_id, muted_where=message.chat_id)
    user = await repo.get()
    if user.muted_until < datetime.now():
        return await repo.delete()

    try:
        await message.ctx_api.messages.delete(
            peer_id=message.peer_id,
            cmids=message.conversation_message_id,
            delete_for_all=True,
        )
    except VKAPIError[15] as ex:
        logger.debug(ex.description)


@labeler.chat_message(text="<_:prefix>muted")
@labeler.chat_message(text="<_:prefix>мутед")
@labeler.chat_message(text="<_:prefix>мьютед")
@labeler.chat_message(text="<_:prefix>мутэд")
@labeler.chat_message(text="<_:prefix>мьютэд")
@labeler.chat_message(text="<_:prefix>inmute")
@labeler.chat_message(text="<_:prefix>вмуте")
@labeler.chat_message(text="<_:prefix>вмьюте")
@labeler.chat_message(text="<_:prefix>замученые")
@labeler.chat_message(text="<_:prefix>замученные")
@labeler.chat_message(text="<_:prefix>замьюченые")
@labeler.chat_message(text="<_:prefix>замьюченные")
@error_handler.catch
async def muted_here_handler(message: Message):
    repo = MutedUserRepository(muted_where=message.chat_id)
    ids = await repo.list_by_muted_where()

    if len(ids) == 0:
        return

    users = await message.ctx_api.users.get(ids, fields=["domain"])

    text = ["В муте:"]

    for user in users:
        text.append(f"{user.first_name} {user.last_name} ({user.domain})")

    return await message.reply("\n".join(text))


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
