from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.handlers.general.fx.bass.bassboost import ALIASES as BASSBOOST_ALIASES
from vkreborn.handlers.general.fx.bass.basscut import ALIASES as BASSCUT_ALIASES
from vkreborn.rules import AliasRule
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import BassEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS}
ALIASES = [
    *BASSBOOST_ALIASES,
    *BASSCUT_ALIASES,
]


@labeler.message(AliasRule(ALIASES, "<gain:gain>"), **defaults)
@error_handler.catch
async def bass_handler(message: Message, gain: float):
    return await make(message, BassEffect(gain=gain))
