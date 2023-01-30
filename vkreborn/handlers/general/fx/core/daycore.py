from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import SpeedEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS, "blocking": False}


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
