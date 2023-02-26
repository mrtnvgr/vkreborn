from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import DupeItemRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = [
    "dupecount",
    "дюпесоунт",
    "дюпекоунт",
    "дюпекаунт",
    "дюпсоунт",
    "дюпкоунт",
    "дюпкаунт",
]


@labeler.chat_message(AliasRule(ALIASES, "<group>"), owner=True)
@error_handler.catch
async def dupecount_handler(message: Message, group: str):
    repo = DupeItemRepository(group=group)
    count = await repo.count_group()
    await message.reply(f'Количество вложений в дюп-группе "{group}": {count}')
