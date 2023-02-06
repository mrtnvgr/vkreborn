from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import DupeItemRepository
from vkreborn.vkbottle import labeler


@labeler.chat_message(text="<_:prefix>dupeclear <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпслеар <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпклеар <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпсклир <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпклир <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеслеар <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеклеар <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпесклир <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеклир <group>", owner=True)
@error_handler.catch
async def dupeclear_handler(message: Message, group: str):
    item_repo = DupeItemRepository(group=group)
    await item_repo.clear_group()
    return await message.reply(f'Кэш дюп-группы "{group}" очищен')
