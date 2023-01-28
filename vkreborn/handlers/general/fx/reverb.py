from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import ReverbEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS, "blocking": False}


@labeler.message(text="<_:prefix>reverb", **defaults)
@error_handler.catch
async def reverb_default_handler(message: Message):
    return await make(message, ReverbEffect())


@labeler.message(text="<_:prefix>reverb <wet:percentage>", **defaults)
@error_handler.catch
async def reverb_wet_handler(message: Message, wet: float):
    return await make(message, ReverbEffect(wet=wet))
