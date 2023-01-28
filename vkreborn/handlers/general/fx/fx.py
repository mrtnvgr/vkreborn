from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import RawEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS, "blocking": False}


@labeler.message(text="<_:prefix>fx <effects>", **defaults)
@labeler.message(text="<_:prefix>фх <effects>", **defaults)
@labeler.message(text="<_:prefix>фкс <effects>", **defaults)
@labeler.message(text="<_:prefix>эфыкс <effects>", **defaults)
@labeler.message(text="<_:prefix>фуфыкс <effects>", **defaults)
@labeler.message(text="<_:prefix>эфых <effects>", **defaults)
@labeler.message(text="<_:prefix>фуфых <effects>", **defaults)
@error_handler.catch
async def fx_handler(message: Message, effects: str):
    return await make(message, RawEffect(effects=effects))
