from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.repositories import MutedUserRepository
from vkbottle.exception_factory import VKAPIError
from datetime import datetime, timedelta
from loguru import logger


@labeler.chat_message(muted=True)
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


@labeler.chat_message(text="<_:prefix>mute <user:mention> <minutes:float>", admin=True)
async def mute_user_handler(message: Message, user: dict, minutes: float):
    muted_until = datetime.now() + timedelta(minutes=minutes)
    repo = MutedUserRepository(
        user_id=user["id"],
        muted_where=message.chat_id,
        muted_by=message.from_id,
        muted_until=muted_until,
    )
    await repo.mute()
    return await message.reply(
        f"Пользователь {user['domain']} замучен до {muted_until.isoformat()}"
    )


@labeler.chat_message(text="<_:prefix>unmute <user:mention>", admin=True)
async def unmute_user_handler(message: Message, user: dict):
    repo = MutedUserRepository(user_id=user["id"], muted_where=message.chat_id)
    await repo.delete()
    return await message.reply(f"Пользователь {user['domain']} размучен")


@labeler.chat_message(text="<_:prefix>muted")
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
async def muted_by_handler(message: Message, user: dict):
    repo = MutedUserRepository(muted_where=message.chat_id, muted_by=user["id"])
    ids = await repo.list_by_muted_by()

    if len(ids) == 0:
        return

    users = await message.ctx_api.users.get(ids, fields=["domain"])

    text = [f"В муте (админом {user['domain']}):"]

    for user in users:
        text.append(f"{user.first_name} {user.last_name} ({user.domain})")

    return await message.reply("\n".join(text))
