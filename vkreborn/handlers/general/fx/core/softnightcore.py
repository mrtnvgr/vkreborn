from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import SpeedEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS, "blocking": False}


@labeler.message(text="<_:prefix>snc", **defaults)
@labeler.message(text="<_:prefix>snk", **defaults)
@labeler.message(text="<_:prefix>снк", **defaults)
@labeler.message(text="<_:prefix>softnightcore", **defaults)
@labeler.message(text="<_:prefix>softnightkore", **defaults)
@labeler.message(text="<_:prefix>софтнайткор", **defaults)
@labeler.message(text="<_:prefix>софтнайткоре", **defaults)
@error_handler.catch
async def softnightcore_handler(message: Message):
    return await make(message, SpeedEffect(speed="softnightcore"))
