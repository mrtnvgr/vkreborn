from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import UserRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = [
    "takemoder",
    "такемодер",
    "такемодерку",
    "тэйкмодер",
    "тэйкмодерку",
    "тейкмодер",
    "тейкмодерку",
    "забратьмодера",
    "забратьмодерку",
    "снятьсмодера",
    "снятьсмодерки",
]


@labeler.chat_message(AliasRule(ALIASES, "<user:mention>"), moder=True)
@error_handler.catch
async def takemoder_handler(message: Message, user: dict):
    repo = UserRepository(user_id=user["id"], chat_id=message.chat_id)

    account = await message.ctx_api.users.get()
    if repo.user_id == account[0].id:
        return await message.reply("...")

    moders = await repo.get_moder_ids()
    if repo.user_id not in moders:
        return await message.reply(
            f"Пользователь {user['domain']} не является модератором", disable_mentions=True
        )

    await repo.set_moder(False)

    return await message.reply(
        f"Пользователь {user['domain']} теперь больше не модератор", disable_mentions=True
    )
