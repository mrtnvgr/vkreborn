from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.repositories import UserRepository
from datetime import datetime, timedelta


@labeler.message(text="<_>mute <user:mention> <minutes:float>", admin=True)
async def mute_user_handler(message: Message, user: dict, minutes: float):
    repo = UserRepository(user_id=user["id"])
    banned_until = datetime.now() + timedelta(minutes=minutes)
    await repo.mute_user_until(banned_until)
    return await message.reply(
        f"Пользователь {user['domain']} замучен до {banned_until.isoformat()}"
    )


@labeler.message(text="<_>unmute <user:mention>", admin=True)
async def unmute_user_handler(message: Message, user: dict):
    repo = UserRepository(user_id=user["id"])
    await repo.mute_user_until(None)
    return await message.reply(f"Пользователь {user['domain']} размучен")
