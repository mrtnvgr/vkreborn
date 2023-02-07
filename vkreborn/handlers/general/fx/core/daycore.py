from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import SpeedEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS}
ALIASES = ["dc", "dk", "дк", "daycore", "daykore", "дейкоре", "дэйкоре", "дейкор", "дэйкор"]


@labeler.message(AliasRule(ALIASES), **defaults)
@error_handler.catch
async def daycore_handler(message: Message):
    return await make(message, SpeedEffect(speed="daycore"))
