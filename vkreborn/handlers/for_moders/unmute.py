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
    await unmute(message=message, user=user)


@labeler.chat_message(AliasRule(ALIASES), reply=True, moder=True)
@error_handler.catch
async def unmute_reply_handler(message: Message):
    user_info = await message.reply_message.get_user(fields=["domain"])
    user = {"id": user_info.id, "domain": f"@{user_info.domain}"}
    await unmute(message=message, user=user)


async def unmute(message: Message, user: dict):
    repo = MutedUserRepository(user_id=user["id"], muted_where=message.chat_id)
    await repo.delete()
    return await message.reply(f"Пользователь {user['domain']} размьючен", disable_mentions=True)
