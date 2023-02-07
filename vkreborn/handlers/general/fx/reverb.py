from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import ReverbEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS}
ALIASES = ["reverb", "реверб", "ревер"]


@labeler.message(AliasRule(ALIASES), **defaults)
@error_handler.catch
async def reverb_default_handler(message: Message):
    return await make(message, ReverbEffect())


@labeler.message(AliasRule(ALIASES, "<wet:factor>"), **defaults)
@error_handler.catch
async def reverb_wet_handler(message: Message, wet: float):
    return await make(message, ReverbEffect(wet=wet))
