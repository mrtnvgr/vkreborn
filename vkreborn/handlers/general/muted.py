from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import MutedUserRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = [
    "muted",
    "мутед",
    "мьютед",
    "мутэд",
    "мьютэд",
    "inmute",
    "вмуте",
    "вмьюте",
    "замученые",
    "замученные",
    "замьюченые",
    "замьюченные",
]


@labeler.chat_message(AliasRule(ALIASES))
@error_handler.catch
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
