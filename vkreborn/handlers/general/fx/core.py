from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import SpeedEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS, "blocking": False}


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
@labeler.message(text="<_:prefix>core <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>kore <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>коре <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>кор <speed:abs_float>", **defaults)
@error_handler.catch
async def core_handler(message: Message, speed: float):
    return await make(message, SpeedEffect(speed=speed))


@labeler.message(text="<_:prefix>nc", **defaults)
@labeler.message(text="<_:prefix>nk", **defaults)
@labeler.message(text="<_:prefix>нк", **defaults)
@labeler.message(text="<_:prefix>nightcore", **defaults)
@labeler.message(text="<_:prefix>nightkore", **defaults)
@labeler.message(text="<_:prefix>найткор", **defaults)
@labeler.message(text="<_:prefix>найткоре", **defaults)
@labeler.message(text="<_:prefix>core", **defaults)
@labeler.message(text="<_:prefix>kore", **defaults)
@labeler.message(text="<_:prefix>коре", **defaults)
@labeler.message(text="<_:prefix>кор", **defaults)
@error_handler.catch
async def nightcore_handler(message: Message):
    return await make(message, SpeedEffect(speed="nightcore"))


@labeler.message(text="<_:prefix>dc", **defaults)
@labeler.message(text="<_:prefix>dk", **defaults)
@labeler.message(text="<_:prefix>дк", **defaults)
@labeler.message(text="<_:prefix>daycore", **defaults)
@labeler.message(text="<_:prefix>daykore", **defaults)
@labeler.message(text="<_:prefix>дейкоре", **defaults)
@labeler.message(text="<_:prefix>дэйкоре", **defaults)
@labeler.message(text="<_:prefix>дейкор", **defaults)
@labeler.message(text="<_:prefix>дэйкор", **defaults)
@error_handler.catch
async def daycore_handler(message: Message):
    return await make(message, SpeedEffect(speed="daycore"))
