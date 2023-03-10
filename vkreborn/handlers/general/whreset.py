from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import WHPictureRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = ["whreset", "вхрезет", "вхрезэт", "вхрэзэт"]


@labeler.private_message(AliasRule(ALIASES))
@error_handler.catch
async def pm_whreset_handler(message: Message):
    repo = WHPictureRepository(where_id=message.chat_id)
    await repo.reset_chat()
    return await message.reply("Кэш комманды wh очищен")
