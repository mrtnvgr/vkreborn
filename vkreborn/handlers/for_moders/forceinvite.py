from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.handlers.for_moders.invite import invite
from vkreborn.handlers.for_moders.kick import kick
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = ["forceinvite", "форсинвайт", "форсеинвайт", "форсинвайте", "форсеинвайте"]


@labeler.chat_message(AliasRule(ALIASES, "<user:mention>"), moder=True)
@error_handler.catch
async def forceinvite_handler(message: Message, user: dict):
    await forceinvite(message=message, user=user)


@labeler.chat_message(AliasRule(ALIASES), reply=True, moder=True)
@error_handler.catch
async def forceinvite_reply_handler(message: Message):
    user_info = await message.reply_message.get_user(fields=["domain"])
    user = {"id": user_info.id, "domain": f"@{user_info.domain}"}
    await forceinvite(message=message, user=user)


async def forceinvite(message: Message, user: dict):
    await kick(message=message, user=user, reply=False)
    await invite(message=message, user_id=user["id"], visible_messages_count=0, reply=False)
