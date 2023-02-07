from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.handlers.general.fx.core.daycore import ALIASES as DAYCORE_ALIASES
from vkreborn.handlers.general.fx.core.nightcore import ALIASES as NIGHTCORE_ALIASES
from vkreborn.handlers.general.fx.core.softdaycore import ALIASES as SOFTDAYCORE_ALIASES
from vkreborn.handlers.general.fx.core.softnightcore import (
    ALIASES as SOFTNIGHTCORE_ALIASES,
)
from vkreborn.rules import AliasRule
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import SpeedEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS}
ALIASES = [
    *NIGHTCORE_ALIASES,
    *DAYCORE_ALIASES,
    *SOFTDAYCORE_ALIASES,
    *SOFTNIGHTCORE_ALIASES,
]


@labeler.message(AliasRule(ALIASES, "<speed:factor>"), **defaults)
@error_handler.catch
async def core_handler(message: Message, speed: float):
    return await make(message, SpeedEffect(speed=speed))
