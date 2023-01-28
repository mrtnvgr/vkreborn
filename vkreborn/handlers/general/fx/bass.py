from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import BassEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS, "blocking": False}


@labeler.message(text="<_:prefix>bassboost <gain:gain>", **defaults)
@labeler.message(text="<_:prefix>бассбуст <gain:gain>", **defaults)
@labeler.message(text="<_:prefix>басбуст <gain:gain>", **defaults)
@labeler.message(text="<_:prefix>basscut <gain:gain>", **defaults)
@labeler.message(text="<_:prefix>басскат <gain:gain>", **defaults)
@labeler.message(text="<_:prefix>баскат <gain:gain>", **defaults)
@labeler.message(text="<_:prefix>басскут <gain:gain>", **defaults)
@labeler.message(text="<_:prefix>баскут <gain:gain>", **defaults)
@labeler.message(text="<_:prefix>bass <gain:gain>", **defaults)
@labeler.message(text="<_:prefix>басс <gain:gain>", **defaults)
@labeler.message(text="<_:prefix>бас <gain:gain>", **defaults)
@error_handler.catch
async def bassboost_handler(message: Message, gain: float):
    return await make(message, BassEffect(gain=gain))


@labeler.message(text="<_:prefix>bassboost", **defaults)
@labeler.message(text="<_:prefix>basscut", **defaults)
@labeler.message(text="<_:prefix>bass", **defaults)
@error_handler.catch
async def bassboost_default_handler(message: Message):
    return await make(message, BassEffect())
