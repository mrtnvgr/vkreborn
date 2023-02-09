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
    await kick(message=message, user=user)
    await invite(message=message, user_id=user["id"])
