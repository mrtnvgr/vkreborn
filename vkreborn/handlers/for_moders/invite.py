from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = ["invite", "инвайт", "инвайте", "пригласить", "добавить"]


@labeler.chat_message(AliasRule(ALIASES, "<user:mention>"), moder=True)
@error_handler.catch
async def invite_handler(message: Message, user: dict):
    await invite(message=message, user=user)


@labeler.chat_message(AliasRule(ALIASES), reply=True, moder=True)
@error_handler.catch
async def invite_reply_handler(message: Message):
    user_info = await message.reply_message.get_user(fields=["domain"])
    user = {"id": user_info.id, "domain": f"@{user_info.domain}"}
    await invite(message=message, user=user)


async def invite(
    message: Message, user: dict, visible_messages_count: int = 250, reply: bool = True
):
    await message.ctx_api.messages.add_chat_user(
        chat_id=message.chat_id,
        user_id=user["id"],
        visible_messages_count=visible_messages_count,
    )
    if reply:
        await message.reply(f"Пользователь {user['domain']} приглашен", disable_mentions=True)
