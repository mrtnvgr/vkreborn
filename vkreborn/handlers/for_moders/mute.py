from datetime import datetime, timedelta

from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import MutedUserRepository, UserRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = ["mute", "муте", "мут", "мьюте", "мьют", "silence", "сайленс"]


@labeler.chat_message(AliasRule(ALIASES, "<user:mention> <minutes:int>"), moder=True)
@error_handler.catch
async def mute_user_handler(message: Message, user: dict, minutes: int):

    repo = UserRepository(user_id=user["id"], chat_id=message.chat_id)
    repo_user = await repo.get_user()

    if repo_user and repo_user.is_moder:
        return await message.reply("Модераторов мьютить нельзя")

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
