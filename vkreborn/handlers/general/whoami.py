from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import UserRepository
from vkreborn.vkbottle import labeler


@labeler.chat_message(text="<_:prefix>whoami")
@labeler.chat_message(text="<_:prefix>вхуамай")
@labeler.chat_message(text="<_:prefix>вхуами")
@labeler.chat_message(text="<_:prefix>хуамай")
@labeler.chat_message(text="<_:prefix>хуами")
@error_handler.catch
async def whoami_handler(message: Message):
    repo = UserRepository(user_id=message.from_id, chat_id=message.chat_id)
    user_info = await repo.get_user()
    response = "Модератор" if user_info.is_moder else "Пользователь"
    return await message.reply(response)
