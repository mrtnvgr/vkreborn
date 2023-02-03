from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import TempoEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS}


@labeler.message(text="<_:prefix>tempo <tempo:factor>", **defaults)
@labeler.message(text="<_:prefix>темпо <tempo:factor>", **defaults)
@labeler.message(text="<_:prefix>темп <tempo:factor>", **defaults)
@labeler.message(text="<_:prefix>темпоу <tempo:factor>", **defaults)
@labeler.message(text="<_:prefix>тэмпо <tempo:factor>", **defaults)
@labeler.message(text="<_:prefix>тэмп <tempo:factor>", **defaults)
@labeler.message(text="<_:prefix>тэмпоу <tempo:factor>", **defaults)
@error_handler.catch
async def tempo_handler(message: Message, tempo: float):
    return await make(message, TempoEffect(tempo=tempo))
