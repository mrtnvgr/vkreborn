from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import UserRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = ["whois", "вхуиз", "вхуис", "хуис", "хуиз"]


@labeler.chat_message(AliasRule(ALIASES, "<user:mention>"))
@error_handler.catch
async def whois_handler(message: Message, user: dict):
    repo = UserRepository(user_id=user["id"], chat_id=message.chat_id)
    user = await repo.get_user()
    is_moder = user.is_moder if user else False
    response = "Модератор" if is_moder else "Пользователь"
    return await message.reply(response)
