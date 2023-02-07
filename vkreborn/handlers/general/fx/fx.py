from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import RawEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS}
ALIASES = ["fx", "фх", "фкс", "эфыкс", "фуфыкс", "эфых", "фуфых"]


@labeler.message(AliasRule(ALIASES, "<effects>"), **defaults)
@error_handler.catch
async def fx_handler(message: Message, effects: str):
    return await make(message, RawEffect(effects=effects))
