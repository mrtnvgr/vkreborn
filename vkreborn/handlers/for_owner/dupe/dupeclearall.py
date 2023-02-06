from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import DupeItemRepository
from vkreborn.vkbottle import labeler


@labeler.chat_message(text="<_:prefix>dupeclearall", owner=True)
@labeler.chat_message(text="<_:prefix>дюпслеаралл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпклеаралл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпсклиралл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпклиралл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеслеаралл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеклеаралл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпесклиралл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеклиралл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпслеаролл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпклеаролл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпсклиролл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпклиролл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеслеаролл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеклеаролл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпесклиролл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеклиролл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпслеарал", owner=True)
@labeler.chat_message(text="<_:prefix>дюпклеарал", owner=True)
@labeler.chat_message(text="<_:prefix>дюпсклирал", owner=True)
@labeler.chat_message(text="<_:prefix>дюпклирал", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеслеарал", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеклеарал", owner=True)
@labeler.chat_message(text="<_:prefix>дюпесклирал", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеклирал", owner=True)
@labeler.chat_message(text="<_:prefix>дюпслеарол", owner=True)
@labeler.chat_message(text="<_:prefix>дюпклеарол", owner=True)
@labeler.chat_message(text="<_:prefix>дюпсклирол", owner=True)
@labeler.chat_message(text="<_:prefix>дюпклирол", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеслеарол", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеклеарол", owner=True)
@labeler.chat_message(text="<_:prefix>дюпесклирол", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеклирол", owner=True)
@error_handler.catch
async def dupeclear_all_handler(message: Message):
    repo = DupeItemRepository()
    await repo.clear_all()
    return await message.reply("Кэш дюп-групп очищен")
