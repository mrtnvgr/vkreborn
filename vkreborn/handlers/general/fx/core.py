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


@labeler.message(text="<_:prefix>snc", **defaults)
@labeler.message(text="<_:prefix>snk", **defaults)
@labeler.message(text="<_:prefix>снк", **defaults)
@labeler.message(text="<_:prefix>softnightcore", **defaults)
@labeler.message(text="<_:prefix>softnightkore", **defaults)
@labeler.message(text="<_:prefix>софтнайткор", **defaults)
@labeler.message(text="<_:prefix>софтнайткоре", **defaults)
async def softnightcore_handler(message: Message):
    return await make(message, SpeedEffect(speed="softnightcore"))


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


@labeler.message(text="<_:prefix>sdc", **defaults)
@labeler.message(text="<_:prefix>sdk", **defaults)
@labeler.message(text="<_:prefix>сдк", **defaults)
@labeler.message(text="<_:prefix>softdaycore", **defaults)
@labeler.message(text="<_:prefix>softdaykore", **defaults)
@labeler.message(text="<_:prefix>софтдейкоре", **defaults)
@labeler.message(text="<_:prefix>софтдэйкоре", **defaults)
@labeler.message(text="<_:prefix>софтдейкор", **defaults)
@labeler.message(text="<_:prefix>софтдэйкор", **defaults)
async def softdaycore_handler(message: Message):
    return await make(message, SpeedEffect(speed="softdaycore"))
