from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.repositories import MutedUserRepository
from vkbottle.exception_factory import VKAPIError
from vkreborn.error_handler import error_handler
from datetime import datetime
from loguru import logger


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


@labeler.chat_message(text="<_:prefix>mutedby <user:mention>")
@error_handler.catch
async def muted_by_handler(message: Message, user: dict):
    repo = MutedUserRepository(muted_where=message.chat_id, muted_by=user["id"])
    ids = await repo.list_by_muted_by()

    if len(ids) == 0:
        return

    users = await message.ctx_api.users.get(ids, fields=["domain"])

    text = [f"В муте (модером {user['domain']}):"]

    for user in users:
        text.append(f"{user.first_name} {user.last_name} ({user.domain})")

    return await message.reply("\n".join(text))
