from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import DupeChatRepository, DupeItemRepository
from vkreborn.vkbottle import labeler


@labeler.chat_message(text="<_:prefix>dupeclearold", owner=True)
@labeler.chat_message(text="<_:prefix>дюпслеаролд", owner=True)
@labeler.chat_message(text="<_:prefix>дюпклеаролд", owner=True)
@labeler.chat_message(text="<_:prefix>дюпсклиролд", owner=True)
@labeler.chat_message(text="<_:prefix>дюпклиролд", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеслеаролд", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеклеаролд", owner=True)
@labeler.chat_message(text="<_:prefix>дюпесклиролд", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеклиролд", owner=True)
@error_handler.catch
async def dupeclear_old_handler(message: Message):
    item_repo = DupeItemRepository()
    chat_repo = DupeChatRepository()
    groups = await chat_repo.get_all_groups()
    await item_repo.clear_old(chat_groups=groups)
    return await message.reply("Кэш неактивных дюп-групп очищен")
