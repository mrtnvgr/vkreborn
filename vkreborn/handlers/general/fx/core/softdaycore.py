from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import SpeedEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS, "blocking": False}


@labeler.message(text="<_:prefix>sdc", **defaults)
@labeler.message(text="<_:prefix>sdk", **defaults)
@labeler.message(text="<_:prefix>сдк", **defaults)
@labeler.message(text="<_:prefix>softdaycore", **defaults)
@labeler.message(text="<_:prefix>softdaykore", **defaults)
@labeler.message(text="<_:prefix>софтдейкоре", **defaults)
@labeler.message(text="<_:prefix>софтдэйкоре", **defaults)
@labeler.message(text="<_:prefix>софтдейкор", **defaults)
@labeler.message(text="<_:prefix>софтдэйкор", **defaults)
@error_handler.catch
async def softdaycore_handler(message: Message):
    return await make(message, SpeedEffect(speed="softdaycore"))
