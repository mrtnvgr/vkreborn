from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import UserRepository
from vkreborn.vkbottle import labeler


@labeler.message(text="<_:prefix>moders")
@labeler.message(text="<_:prefix>модеры")
@error_handler.catch
async def moders_handler(message: Message):
    repo = UserRepository(user_id=message.from_id, chat_id=message.chat_id)
    moder_ids = await repo.get_moder_ids()

    moders_info = await message.ctx_api.users.get(moder_ids, fields=["domain"])

    moders = [f"{moder.first_name} {moder.last_name} ({moder.domain})" for moder in moders_info]
    moders.insert(0, "Модераторы:" if len(moders) > 1 else "Модератор:")

    return await message.reply("\n".join(moders))
