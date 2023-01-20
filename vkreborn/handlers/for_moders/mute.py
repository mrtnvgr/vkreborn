from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.repositories import UserRepository, MutedUserRepository
from vkreborn.error_handler import error_handler
from datetime import datetime, timedelta


@labeler.chat_message(text="<_:prefix>mute <user:mention> <minutes:float>", moder=True)
@error_handler.catch
async def mute_user_handler(message: Message, user: dict, minutes: float):

    repo = UserRepository(user_id=user["id"], chat_id=message.chat_id)
    repo_user = await repo.get_user()

    if repo_user and repo_user.is_moder:
        return

    muted_until = datetime.now() + timedelta(minutes=minutes)
    repo = MutedUserRepository(
        user_id=user["id"],
        muted_where=message.chat_id,
        muted_by=message.from_id,
        muted_until=muted_until,
    )
    await repo.mute()

    formatted_date = muted_until.strftime("%H:%M:%S %d.%m.%Y")

    return await message.reply(
        f"Пользователь {user['domain']} замьючен до {formatted_date}",
    )


@labeler.chat_message(text="<_:prefix>unmute <user:mention>", moder=True)
@error_handler.catch
async def unmute_user_handler(message: Message, user: dict):
    repo = MutedUserRepository(user_id=user["id"], muted_where=message.chat_id)
    await repo.delete()
    return await message.reply(f"Пользователь {user['domain']} размьючен")
