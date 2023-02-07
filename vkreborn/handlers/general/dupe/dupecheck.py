from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import DupeChatRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = ["dupecheck", "дюпсческ", "дюпчек", "дюпесческ", "дюпечек"]


@labeler.chat_message(AliasRule(ALIASES))
@error_handler.catch
async def dupechatgroups_handler(message: Message):
    repo = DupeChatRepository(chat_id=message.chat_id)
    groups = await repo.get_chat_groups()

    if not groups:
        return await message.reply("Текущий чат не состоит в дюп-группах")

    word = "Дюп-группа" if len(groups) == 1 else "Дюп-группы"
    groups = [f'"{group}"' for group in groups]
    await message.reply(f"{word} чата: {', '.join(groups)}")
