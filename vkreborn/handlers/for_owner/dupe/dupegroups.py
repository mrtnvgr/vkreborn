from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import DupeChatRepository
from vkreborn.vkbottle import labeler


@labeler.chat_message(text="<_:prefix>dupegroups", owner=True)
@labeler.chat_message(text="<_:prefix>дюпгроупс", owner=True)
@labeler.chat_message(text="<_:prefix>дюпгрупс", owner=True)
@labeler.chat_message(text="<_:prefix>дюпегроупс", owner=True)
@labeler.chat_message(text="<_:prefix>дюпегрупс", owner=True)
@error_handler.catch
async def dupegroups_handler(message: Message):
    repo = DupeChatRepository()
    groups = await repo.get_all_groups()

    if not groups:
        return await message.reply("Активных дюп-групп нет")

    word = "Активные дюп-группы" if len(groups) > 1 else "Активная дюп-группа"
    groups = [f'"{group}"' for group in groups]
    await message.reply(f"{word}: {', '.join(groups)}")
