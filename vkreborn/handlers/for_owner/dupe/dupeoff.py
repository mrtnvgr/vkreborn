from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import DupeChatRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = [
    "dupedelete",
    "dupeoff",
    "dupedisable",
    "дюпделете",
    "дюпделет",
    "дюпделит",
    "дюпделите",
    "дюпдилите",
    "дюпдилит",
    "дюпофф",
    "дюпоф",
    "дюпдизабле",
    "дюпдезабле",
    "дюпдезейбл",
    "дюпдезайбл",
    "дюпеделете",
    "дюпеделет",
    "дюпеделит",
    "дюпеделите",
    "дюпедилите",
    "дюпедилит",
    "дюпеофф",
    "дюпеоф",
    "дюпедизабле",
    "дюпедезабле",
    "дюпедезейбл",
    "дюпедезайбл",
]


@labeler.chat_message(AliasRule(ALIASES), owner=True)
@error_handler.catch
async def dupeoff_all_handler(message: Message):
    repo = DupeChatRepository(chat_id=message.chat_id)

    if not await repo.get_chat_groups():
        return await message.reply("Текущий чат не состоит дюп-группах")

    await repo.delete_from_all_groups()
    return await message.reply("Текущий чат удален из всех дюп-групп")


@labeler.chat_message(AliasRule(ALIASES, "<group>"), owner=True)
@error_handler.catch
async def dupeoff_one_handler(message: Message, group: str):
    repo = DupeChatRepository(chat_id=message.chat_id, group=group)

    if not await repo.check_group():
        return await message.reply(f'Текущий чат не состоит в группе "{group}"')

    await repo.delete_from_group()
    return await message.reply(f'Текущий чат удален из дюп-группы "{group}"')
