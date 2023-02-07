from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import DupeChatRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = [
    "dupeadd",
    "dupeon",
    "dupeenable",
    "dupeset",
    "дюпадд",
    "дюпад",
    "дюпон",
    "дюпенабле",
    "дюпенейбл",
    "дюпенабл",
    "дюпэнабле",
    "дюпэнейбл",
    "дюпэнабл",
    "дюпэнэйбл",
    "дюпеадд",
    "дюпеад",
    "дюпеон",
    "дюпеенабле",
    "дюпеенейбл",
    "дюпеенабл",
    "дюпеэнабле",
    "дюпеэнейбл",
    "дюпеэнабл",
    "дюпеэнэйбл",
]


@labeler.chat_message(AliasRule(ALIASES, "<group>"), owner=True)
@error_handler.catch
async def dupeon_handler(message: Message, group: str):
    repo = DupeChatRepository(chat_id=message.chat_id, group=group)

    if await repo.check_group():
        return await message.reply("Текущий чат уже находится в этой дюп-группе")

    await repo.add()

    return await message.reply(f'Текущий чат теперь в дюп-группе "{group}"')
