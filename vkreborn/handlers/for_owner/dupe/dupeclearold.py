from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import DupeChatRepository, DupeItemRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = [
    "dupeclearold",
    "дюпслеаролд",
    "дюпклеаролд",
    "дюпсклиролд",
    "дюпклиролд",
    "дюпеслеаролд",
    "дюпеклеаролд",
    "дюпесклиролд",
    "дюпеклиролд",
]


@labeler.chat_message(AliasRule(ALIASES), owner=True)
@error_handler.catch
async def dupeclear_old_handler(message: Message):
    item_repo = DupeItemRepository()
    chat_repo = DupeChatRepository()
    groups = await chat_repo.get_all_groups()
    await item_repo.clear_old(chat_groups=groups)
    return await message.reply("Кэш неактивных дюп-групп очищен")
