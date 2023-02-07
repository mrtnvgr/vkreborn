from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import WHPictureRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = [
    "whreset",
    "wallhavenreset",
    "вхрезет",
    "валлхавенрезет",
    "воллхавенрезет",
    "валхавенрезет",
    "волхавенрезет",
    "валлхавэнрезет",
    "воллхавэнрезет",
    "валхавэнрезет",
    "волхавэнрезет",
    "валлхавнрезет",
    "воллхавнрезет",
    "валхавнрезет",
    "волхавнрезет",
    "вхресет",
    "валлхавенресет",
    "воллхавенресет",
    "валхавенресет",
    "волхавенресет",
    "валлхавэнресет",
    "воллхавэнресет",
    "валхавэнресет",
    "волхавэнресет",
    "валлхавнресет",
    "воллхавнресет",
    "валхавнресет",
    "волхавнресет",
]


@labeler.chat_message(AliasRule(ALIASES), moder=True)
@error_handler.catch
async def whreset_handler(message: Message):
    repo = WHPictureRepository(where_id=message.chat_id)
    await repo.reset_chat()
    return await message.reply("Кэш комманды wh очищен")
