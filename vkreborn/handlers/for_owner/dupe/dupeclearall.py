from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import DupeItemRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = [
    "dupeclearall",
    "дюпслеаралл",
    "дюпклеаралл",
    "дюпсклиралл",
    "дюпклиралл",
    "дюпеслеаралл",
    "дюпеклеаралл",
    "дюпесклиралл",
    "дюпеклиралл",
    "дюпслеаролл",
    "дюпклеаролл",
    "дюпсклиролл",
    "дюпклиролл",
    "дюпеслеаролл",
    "дюпеклеаролл",
    "дюпесклиролл",
    "дюпеклиролл",
    "дюпслеарал",
    "дюпклеарал",
    "дюпсклирал",
    "дюпклирал",
    "дюпеслеарал",
    "дюпеклеарал",
    "дюпесклирал",
    "дюпеклирал",
    "дюпслеарол",
    "дюпклеарол",
    "дюпсклирол",
    "дюпклирол",
    "дюпеслеарол",
    "дюпеклеарол",
    "дюпесклирол",
    "дюпеклирол",
]


@labeler.chat_message(AliasRule(ALIASES), owner=True)
@error_handler.catch
async def dupeclear_all_handler(message: Message):
    repo = DupeItemRepository()
    await repo.clear_all()
    return await message.reply("Кэш дюп-групп очищен")
