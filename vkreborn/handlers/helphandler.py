from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.error_handler import error_handler


@labeler.message(text="<_:prefix>help", blocking=False)
@error_handler.catch
async def help_handler(message: Message):
    url = "https://github.com/mrtnvgr/vkreborn/blob/main/docs/index.md"
    return await message.reply(url)
