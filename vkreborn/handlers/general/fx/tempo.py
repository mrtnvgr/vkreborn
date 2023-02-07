from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import TempoEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS}
ALIASES = ["tempo", "темпо", "темп", "темпоу", "тэмпо", "тэмп", "тэмпоу"]


@labeler.message(AliasRule(ALIASES), **defaults)
@error_handler.catch
async def tempo_handler(message: Message, tempo: float):
    return await make(message, TempoEffect(tempo=tempo))
