from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import ReverseEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS}


@labeler.message(text="<_:prefix>reverse", **defaults)
@labeler.message(text="<_:prefix>реверс", **defaults)
@error_handler.catch
async def reverse_handler(message: Message):
    return await make(message, ReverseEffect())
