from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.thirdparty.sox import SUPPORTED_ATTACHMENTS, make
from vkreborn.thirdparty.sox.effects import VolumeEffect
from vkreborn.vkbottle import labeler

defaults = {"attachment": SUPPORTED_ATTACHMENTS}
ALIASES = [
    "volume",
    "вольюм",
    "волюме",
    "волъюм",
    "vol",
    "вол",
    "громкость",
    "gain",
    "гайн",
    "гейн",
    "гэйн",
    "гаин",
    "геин",
    "гэин",
]


@labeler.message(AliasRule(ALIASES, "<volume:gain>"), **defaults)
@error_handler.catch
async def volume_handler(message: Message, volume: float):
    return await make(message, VolumeEffect(volume=volume))
