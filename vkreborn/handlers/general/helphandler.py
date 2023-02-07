from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler


@labeler.message(AliasRule(["help", "хэлп", "хелп"]))
@error_handler.catch
async def help_handler(message: Message):
    url = "https://github.com/mrtnvgr/vkreborn/blob/main/docs/index.md"
    return await message.reply(url)
