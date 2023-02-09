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
    kick_resp = await kick(message=message, user=user)
    if kick_resp:
        await message.reply(f"Пользователь {user['domain']} исключен", disable_mentions=True)


async def kick(message: Message, user: dict):
    repo = UserRepository(user_id=user["id"], chat_id=message.chat_id)

    moders = await repo.get_moder_ids()
    if repo.user_id in moders:
        await message.reply("Модератора нельзя исключить из беседы")
        return False

    try:
        await message.ctx_api.messages.remove_chat_user(
            chat_id=message.chat_id, user_id=user["id"]
        )
        return True
    except VKAPIError[935]:
        await message.reply(
            f"Пользователь {user['domain']} не состоит в беседе", disable_mentions=True
        )
        return False
