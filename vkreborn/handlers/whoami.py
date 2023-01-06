from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.repositories import UserRepository
from vkreborn.error_handler import error_handler


@labeler.message(text="<_:prefix>whoami")
@error_handler.catch
async def whoami_handler(message: Message):
    repo = UserRepository(user_id=message.from_id, chat_id=message.chat_id)
    user_info = await repo.get_user()
    response = "Админ" if user_info.is_admin else "Пользователь"
    return await message.reply(response)
