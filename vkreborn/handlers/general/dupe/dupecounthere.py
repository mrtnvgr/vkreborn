from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.handlers.for_owner.dupe.dupecount import compile_results
from vkreborn.repositories import DupeChatRepository, DupeItemRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = [
    "dupecounthere",
    "дюпесоунтхере",
    "дюпесоунтхир",
    "дюпесоунтхер",
    "дюпекоунтхере",
    "дюпекоунтхир",
    "дюпекоунтхер",
    "дюпекаунтхере",
    "дюпекаунтхир",
    "дюпекаунтхер",
    "дюпсоунтхере",
    "дюпсоунтхир",
    "дюпсоунтхере",
    "дюпкоунтхере",
    "дюпкоунтхир",
    "дюпкоунтхер",
    "дюпкаунтхере",
    "дюпкаунтхир",
    "дюпкаунтхер",
]


@labeler.chat_message(AliasRule(ALIASES))
@error_handler.catch
async def dupecounthere_handler(message: Message):
    dupe_chat_repo = DupeChatRepository(chat_id=message.chat_id)
    dupe_item_repo = DupeItemRepository()

    chat_groups = await dupe_chat_repo.get_chat_groups()
    results = await dupe_item_repo.count_groups(groups=chat_groups)

    reply = await compile_results(results=results)
    await message.reply(reply)
