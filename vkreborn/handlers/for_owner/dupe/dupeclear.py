from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import DupeItemRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = [
    "dupeclear",
    "дюпслеар",
    "дюпклеар",
    "дюпсклир",
    "дюпклир",
    "дюпеслеар",
    "дюпеклеар",
    "дюпесклир",
    "дюпеклир",
]


@labeler.chat_message(AliasRule(ALIASES, "<group>"), owner=True)
@error_handler.catch
async def dupeclear_handler(message: Message, group: str):
    item_repo = DupeItemRepository(group=group)
    await item_repo.clear_group()
    return await message.reply(f'Кэш дюп-группы "{group}" очищен')
