from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import SpeedEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS}


@labeler.message(text="<_:prefix>nc <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>nk <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>нк <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>nightcore <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>nightkore <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>найткор <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>найткоре <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>dc <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>dk <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>дк <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>daycore <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>daykore <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>дейкоре <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>дэйкоре <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>дейкор <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>дэйкор <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>sdc <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>sdk <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>сдк <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>softdaycore <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>softdaykore <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>софтдейкоре <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>софтдэйкоре <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>софтдейкор <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>софтдэйкор <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>core <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>kore <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>коре <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>кор <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>snc <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>snk <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>снк <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>softnightcore <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>softnightkore <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>софтнайткор <speed:factor>", **defaults)
@labeler.message(text="<_:prefix>софтнайткоре <speed:factor>", **defaults)
@error_handler.catch
async def core_handler(message: Message, speed: float):
    return await make(message, SpeedEffect(speed=speed))
