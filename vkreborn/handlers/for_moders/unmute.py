from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import MutedUserRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = [
    "unmute",
    "унмуте",
    "унмут",
    "унмьюте",
    "унмьют",
    "анмуте",
    "анмут",
    "анмьюте",
    "анмьют",
]


@labeler.chat_message(AliasRule(ALIASES, "<user:mention>"), moder=True)
@error_handler.catch
async def unmute_user_handler(message: Message, user: dict):
    repo = MutedUserRepository(user_id=user["id"], muted_where=message.chat_id)
    await repo.delete()
    return await message.reply(f"Пользователь {user['domain']} размьючен", disable_mentions=True)
