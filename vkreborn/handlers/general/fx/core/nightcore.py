from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import SpeedEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS}


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
