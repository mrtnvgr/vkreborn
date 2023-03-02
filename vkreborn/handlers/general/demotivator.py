from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

SUPPORTED_ATTACHMENTS = ["photo"]
defaults = {"attachment": SUPPORTED_ATTACHMENTS}


@labeler.message(AliasRule(["dm", "дм", "demotivator", "демотиватор"], "<text:list>"), **defaults)
@error_handler.catch
async def dm_default_handler(message: Message, _: list):
    # TODO: implement
    await message.reply("Демотиваторы временно отключены")
