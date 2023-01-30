from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import UserRepository
from vkreborn.vkbottle import labeler


@labeler.chat_message(text="<_:prefix>whois <user:mention>")
@labeler.chat_message(text="<_:prefix>вхуиз <user:mention>")
@labeler.chat_message(text="<_:prefix>вхуис <user:mention>")
@labeler.chat_message(text="<_:prefix>хуис <user:mention>")
@labeler.chat_message(text="<_:prefix>хуиз <user:mention>")
@error_handler.catch
async def whois_handler(message: Message, user: dict):
    repo = UserRepository(user_id=user["id"], chat_id=message.chat_id)
    user = await repo.get_user()
    is_moder = user.is_moder if user else False
    response = "Модератор" if is_moder else "Пользователь"
    return await message.reply(response)
