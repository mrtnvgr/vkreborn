from vkbottle import VKAPIError
from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import UserRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = ["kick", "кик", "кикнуть", "исключить"]


@labeler.chat_message(AliasRule(ALIASES, "<user:mention>"), moder=True)
@error_handler.catch
async def kick_handler(message: Message, user: dict):
    await kick(message=message, user=user)


@labeler.chat_message(AliasRule(ALIASES), reply=True, moder=True)
@error_handler.catch
async def kick_reply_handler(message: Message):
    user_info = await message.reply_message.get_user(fields=["domain"])
    user = {"id": user_info.id, "domain": f"@{user_info.domain}"}
    await kick(message=message, user=user)


async def kick(message: Message, user: dict, reply: bool = True):
    repo = UserRepository(user_id=user["id"], chat_id=message.chat_id)

    moders = await repo.get_moder_ids()
    if repo.user_id in moders:
        return await message.reply("Модератора нельзя исключить из беседы")

    try:
        await message.ctx_api.messages.remove_chat_user(
            chat_id=message.chat_id, user_id=user["id"]
        )
        if reply:
            await message.reply(f"Пользователь {user['domain']} исключен", disable_mentions=True)
    except VKAPIError[935]:
        await message.reply(
            f"Пользователь {user['domain']} не состоит в беседе", disable_mentions=True
        )
