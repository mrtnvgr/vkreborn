from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = ["invite", "инвайт", "инвайте", "пригласить", "добавить"]


@labeler.chat_message(AliasRule(ALIASES, "<user:mention>"), moder=True)
@error_handler.catch
async def invite_handler(message: Message, user: dict):
    await invite(message=message, user_id=user["id"])
    return await message.reply(f"Пользователь {user['domain']} приглашен")


async def invite(message: Message, user_id: int, visible_messages_count: int = 250):
    await message.ctx_api.messages.add_chat_user(
        chat_id=message.chat_id,
        user_id=user_id,
        visible_messages_count=visible_messages_count,
    )
