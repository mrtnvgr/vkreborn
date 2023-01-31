from datetime import datetime, timedelta

from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import MutedUserRepository, UserRepository
from vkreborn.vkbottle import labeler


@labeler.chat_message(text="<_:prefix>mute <user:mention> <minutes:int>", moder=True)
@labeler.chat_message(text="<_:prefix>муте <user:mention> <minutes:int>", moder=True)
@labeler.chat_message(text="<_:prefix>мут <user:mention> <minutes:int>", moder=True)
@labeler.chat_message(text="<_:prefix>мьюте <user:mention> <minutes:int>", moder=True)
@labeler.chat_message(text="<_:prefix>мьют <user:mention> <minutes:int>", moder=True)
@labeler.chat_message(text="<_:prefix>silence <user:mention> <minutes:int>", moder=True)
@labeler.chat_message(text="<_:prefix>сайленс <user:mention> <minutes:int>", moder=True)
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
@labeler.chat_message(text="<_:prefix>унмуте <user:mention>", moder=True)
@labeler.chat_message(text="<_:prefix>унмут <user:mention>", moder=True)
@labeler.chat_message(text="<_:prefix>унмьюте <user:mention>", moder=True)
@labeler.chat_message(text="<_:prefix>унмьют <user:mention>", moder=True)
@labeler.chat_message(text="<_:prefix>анмуте <user:mention>", moder=True)
@labeler.chat_message(text="<_:prefix>анмут <user:mention>", moder=True)
@labeler.chat_message(text="<_:prefix>анмьюте <user:mention>", moder=True)
@labeler.chat_message(text="<_:prefix>анмьют <user:mention>", moder=True)
@error_handler.catch
async def unmute_user_handler(message: Message, user: dict):
    repo = MutedUserRepository(user_id=user["id"], muted_where=message.chat_id)
    await repo.delete()
    return await message.reply(f"Пользователь {user['domain']} размьючен")
