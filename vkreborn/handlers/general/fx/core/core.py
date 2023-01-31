from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import SpeedEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS}


@labeler.message(text="<_:prefix>nc <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>nk <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>нк <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>nightcore <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>nightkore <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>найткор <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>найткоре <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>dc <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>dk <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>дк <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>daycore <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>daykore <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>дейкоре <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>дэйкоре <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>дейкор <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>дэйкор <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>sdc <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>sdk <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>сдк <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>softdaycore <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>softdaykore <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>софтдейкоре <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>софтдэйкоре <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>софтдейкор <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>софтдэйкор <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>core <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>kore <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>коре <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>кор <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>snc <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>snk <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>снк <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>softnightcore <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>softnightkore <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>софтнайткор <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>софтнайткоре <speed:abs_float>", **defaults)
@error_handler.catch
async def core_handler(message: Message, speed: float):
    return await make(message, SpeedEffect(speed=speed))
