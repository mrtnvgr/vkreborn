from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import BassEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS}
ALIASES = [
    "basscut",
    "басскат",
    "баскат",
    "басскут",
    "баскут",
]


@labeler.message(AliasRule(ALIASES), **defaults)
@error_handler.catch
async def basscut_default_handler(message: Message):
    return await make(message, BassEffect("basscut"))
