from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import DupeChatRepository
from vkreborn.vkbottle import labeler


@labeler.chat_message(text="<_:prefix>dupecheck")
@labeler.chat_message(text="<_:prefix>дюпсческ")
@labeler.chat_message(text="<_:prefix>дюпчек")
@labeler.chat_message(text="<_:prefix>дюпесческ")
@labeler.chat_message(text="<_:prefix>дюпечек")
@error_handler.catch
async def dupechatgroups_handler(message: Message):
    repo = DupeChatRepository(chat_id=message.chat_id)
    groups = await repo.get_chat_groups()

    if not groups:
        return await message.reply("Текущий чат не состоит в дюп-группах")

    word = "Дюп-группа" if len(groups) == 1 else "Дюп-группы"
    groups = [f'"{group}"' for group in groups]
    await message.reply(f"{word} чата: {', '.join(groups)}")
