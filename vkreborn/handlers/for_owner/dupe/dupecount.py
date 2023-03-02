from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import DupeChatRepository, DupeItemRepository
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
    reply = await compile_results(results=[count])
    await message.reply(reply)


@labeler.chat_message(AliasRule(ALIASES, "<groups:list>"), owner=True)
@error_handler.catch
async def dupecount_groups_handler(message: Message, groups: list[str]):
    repo = DupeItemRepository()
    results = await repo.count_groups(groups=groups)
    reply = await compile_results(results=results)
    await message.reply(reply)


@labeler.chat_message(AliasRule(ALIASES), owner=True)
@error_handler.catch
async def dupecount_handler(message: Message):
    dupe_item_repo = DupeItemRepository()
    dupe_chat_repo = DupeChatRepository()
    groups = await dupe_chat_repo.get_all_groups()
    results = await dupe_item_repo.count_groups(groups=groups)
    reply = await compile_results(results=results)
    await message.reply(reply)


async def compile_results(results: list[str]):
    if len(results) > 1:
        answer = [f'"{group}": {count}' for group, count in results.items()]
        answer.insert(0, "Количество вложений в дюп-группах:\n")
        return "\n".join(answer)
    else:
        group, count = list(results.items())[0]
        return f'Количество вложений в дюп-группе "{group}": {count}'
