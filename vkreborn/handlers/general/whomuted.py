from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import MutedUserRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = [
    "whomuted",
    "хумутед",
    "хумутэд",
    "хумьютед",
    "хумьютэд",
    "вхумутед",
    "вхумутэд",
    "вхумьютед",
    "вхумьютэд",
]


@labeler.chat_message(AliasRule(ALIASES, "<user:mention>"))
@error_handler.catch
async def whomuted_handler(message: Message, user: dict):
    repo = MutedUserRepository(user_id=user["id"], muted_where=message.chat_id)
    user_info = await repo.get()

    if not user_info:
        return await message.reply(
            f"Пользователь {user['domain']} не замьючен", disable_mentions=True
        )

    moder = (await message.ctx_api.users.get(user_info.muted_by, fields=["domain"]))[0]
    moder_info = f"{moder.first_name} {moder.last_name} ({moder.domain})"
    return await message.reply(
        f"Пользователя {user['domain']} замьютил:\n{moder_info}", disable_mentions=True
    )
