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


@labeler.chat_message(AliasRule(ALIASES, "<group:literally_str>"), owner=True)
@error_handler.catch
async def dupecount_group_handler(message: Message, group: str):
    repo = DupeItemRepository(group=group)
    count = await repo.count_group()
    await message.reply(f'Количество вложений в дюп-группе "{group}": {count}')


@labeler.chat_message(AliasRule(ALIASES, "<groups:list>"), owner=True)
@error_handler.catch
async def dupecount_groups_handler(message: Message, groups: list[str]):
    repo = DupeItemRepository()
    results = await repo.count_groups(groups=groups)

    answer = [f'"{group}": {count}' for group, count in results.items()]
    answer.insert(0, "Количество вложений в дюп-группах:\n")
    await message.reply("\n".join(answer))
