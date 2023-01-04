from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.repositories import MutedUserRepository
from datetime import datetime, timedelta


@labeler.message(text="<_>mute <user:mention> <minutes:float>", admin=True)
async def mute_user_handler(message: Message, user: dict, minutes: float):
    muted_until = datetime.now() + timedelta(minutes=minutes)
    repo = MutedUserRepository(
        user_id=user["id"], muted_where=message.chat_id, muted_until=muted_until
    )
    await repo.mute()
    return await message.reply(
        f"Пользователь {user['domain']} замучен до {muted_until.isoformat()}"
    )


@labeler.message(text="<_>unmute <user:mention>", admin=True)
async def unmute_user_handler(message: Message, user: dict):
    repo = MutedUserRepository(user_id=user["id"], muted_where=message.chat_id)
    await repo.delete()
    return await message.reply(f"Пользователь {user['domain']} размучен")
