from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import TempoEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS}


@labeler.message(text="<_:prefix>tempo <tempo:abs_float>", **defaults)
@labeler.message(text="<_:prefix>темпо <tempo:abs_float>", **defaults)
@labeler.message(text="<_:prefix>темп <tempo:abs_float>", **defaults)
@labeler.message(text="<_:prefix>темпоу <tempo:abs_float>", **defaults)
@labeler.message(text="<_:prefix>тэмпо <tempo:abs_float>", **defaults)
@labeler.message(text="<_:prefix>тэмп <tempo:abs_float>", **defaults)
@labeler.message(text="<_:prefix>тэмпоу <tempo:abs_float>", **defaults)
@error_handler.catch
async def tempo_handler(message: Message, tempo: float):
    return await make(message, TempoEffect(tempo=tempo))
