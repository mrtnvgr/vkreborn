from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.error_handler import error_handler
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import (
    SpeedEffect,
    BassEffect,
    ReverseEffect,
    RawEffect,
)

defaults = {"attachment": SUPPORTED_ATTACHMENTS, "blocking": False}


@labeler.message(text="<_:prefix>fx <effects>", **defaults)
@error_handler.catch
async def fx_handler(message: Message, effects: str):
    return await make(message, RawEffect(effects=effects))


@labeler.message(text="<_:prefix>nc <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>nightcore <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>dc <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>daycore <speed:abs_float>", **defaults)
@labeler.message(text="<_:prefix>core <speed:abs_float>", **defaults)
@error_handler.catch
async def core_handler(message: Message, speed: float):
    return await make(message, SpeedEffect(speed=speed))


@labeler.message(text="<_:prefix>nc", **defaults)
@labeler.message(text="<_:prefix>nightcore", **defaults)
@labeler.message(text="<_:prefix>core", **defaults)
@error_handler.catch
async def nightcore_handler(message: Message):
    return await make(message, SpeedEffect(speed="nightcore"))


@labeler.message(text="<_:prefix>dc", **defaults)
@labeler.message(text="<_:prefix>daycore", **defaults)
@error_handler.catch
async def daycore_handler(message: Message):
    return await make(message, SpeedEffect(speed="daycore"))


@labeler.message(text="<_:prefix>bassboost <gain:float>", **defaults)
@labeler.message(text="<_:prefix>basscut <gain:float>", **defaults)
@labeler.message(text="<_:prefix>bass <gain:float>", **defaults)
@error_handler.catch
async def bassboost_handler(message: Message, gain: float):
    return await make(message, BassEffect(gain=gain))


@labeler.message(text="<_:prefix>bassboost", **defaults)
@labeler.message(text="<_:prefix>basscut", **defaults)
@labeler.message(text="<_:prefix>bass", **defaults)
@error_handler.catch
async def bassboost_default_handler(message: Message):
    return await make(message, BassEffect())


@labeler.message(text="<_:prefix>reverse", **defaults)
@error_handler.catch
async def reverse_handler(message: Message):
    return await make(message, ReverseEffect())


# @labeler.message(text="<_:prefix>reverb", **defaults)
# @error_handler.catch
# async def reverb_default_handler(message: Message):
#     return await make(message, reverb_def=True)


# @labeler.message(text="<_:prefix>reverb <wet:percentage>", **defaults)
# @error_handler.catch
# async def reverb_handler(message: Message, wet: int):
#     return await make(message, reverb=wet)
