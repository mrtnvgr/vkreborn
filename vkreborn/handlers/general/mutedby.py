from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import MutedUserRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = ["mutedby", "мутедбай", "мутэдбай", "мьютедбай", "мьютэдбай"]


@labeler.chat_message(AliasRule(ALIASES, "<user:mention>"))
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

    return await message.reply("\n".join(text), disable_mentions=True)
