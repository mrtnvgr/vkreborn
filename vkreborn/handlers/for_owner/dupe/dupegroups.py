from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import DupeChatRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = ["dupegroups", "дюпгроупс", "дюпгрупс", "дюпегроупс", "дюпегрупс"]


@labeler.chat_message(AliasRule(ALIASES), owner=True)
@error_handler.catch
async def dupegroups_handler(message: Message):
    repo = DupeChatRepository()
    groups = await repo.get_all_groups()

    if not groups:
        return await message.reply("Активных дюп-групп нет")

    word = "Активные дюп-группы" if len(groups) > 1 else "Активная дюп-группа"
    groups = [f'"{group}"' for group in groups]
    await message.reply(f"{word}: {', '.join(groups)}")
