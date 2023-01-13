from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.error_handler import error_handler


@labeler.message(text="<_:prefix>wh", blocking=False)
@error_handler.catch
async def wh_noargs_handler(message: Message):
    attachment = await get_picture()
    return await message.reply(attachment=attachment)


async def get_picture(q:str = "", categories: str = "", purity: str = "100"):
    pass
