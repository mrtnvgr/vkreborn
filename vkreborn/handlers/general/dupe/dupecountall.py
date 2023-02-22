from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import DupeItemRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = [
    "dupecountall",
    "дюпесоунталл",
    "дюпесоунтал",
    "дюпесоунтол",
    "дюпесоунтолл",
    "дюпсоунталл",
    "дюпсоунтал",
    "дюпсоунтол",
    "дюпсоунтолл",
    "дюпекоунталл",
    "дюпекоунтал",
    "дюпекоунтол",
    "дюпекоунтолл",
    "дюпекоунталл",
    "дюпекоунтал",
    "дюпекоунтол",
    "дюпекоунтолл",
    "дюпекаунталл",
    "дюпекаунтал",
    "дюпекаунтол",
    "дюпекаунтолл",
    "дюпекаунталл",
    "дюпекаунтал",
    "дюпекаунтол",
    "дюпекаунтолл",
    "дюпсоунталл",
    "дюпсоунтал",
    "дюпсоунтол",
    "дюпсоунтолл",
    "дюпсоунталл",
    "дюпсоунтал",
    "дюпсоунтол",
    "дюпсоунтолл",
    "дюпкоунталл",
    "дюпкоунтал",
    "дюпкоунтол",
    "дюпкоунтолл",
    "дюпкоунталл",
    "дюпкоунтал",
    "дюпкоунтол",
    "дюпкоунтолл",
    "дюпкаунталл",
    "дюпкаунтал",
    "дюпкаунтол",
    "дюпкаунтолл",
    "дюпкаунталл",
    "дюпкаунтал",
    "дюпкаунтол",
    "дюпкаунтолл",
]


@labeler.chat_message(AliasRule(ALIASES))
@error_handler.catch
async def dupecount_all_handler(message: Message):
    repo = DupeItemRepository()
    count = await repo.count_all()
    await message.reply(f"Количество вложений со всех дюп-групп: {count}")
