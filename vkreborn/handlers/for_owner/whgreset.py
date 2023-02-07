from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import WHPictureRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = [
    "whgreset",
    "wallhavengreset",
    "wallhavenglobalreset",
    "вхгрезет",
    "валлхавенгрезет",
    "воллхавенгрезет",
    "валхавенгрезет",
    "волхавенгрезет",
    "валлхавэнгрезет",
    "воллхавэнгрезет",
    "валхавэнгрезет",
    "волхавэнгрезет",
    "валлхавнгрезет",
    "воллхавнгрезет",
    "валхавнгрезет",
    "волхавнгрезет",
    "вхгресет",
    "валлхавенгресет",
    "воллхавенгресет",
    "валхавенгресет",
    "волхавенгресет",
    "валлхавэнгресет",
    "воллхавэнгресет",
    "валхавэнгресет",
    "волхавэнгресет",
    "валлхавнгресет",
    "воллхавнгресет",
    "валхавнгресет",
    "волхавнгресет",
]


@labeler.message(AliasRule(ALIASES), owner=True)
@error_handler.catch
async def whgreset_handler(message: Message):
    repo = WHPictureRepository()
    await repo.reset_all()
    return await message.reply("Кэш комманды wh очищен глобально")
