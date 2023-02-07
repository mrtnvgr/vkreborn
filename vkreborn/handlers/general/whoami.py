from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import UserRepository
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = ["whoami", "вхуамай", "вхуами", "хуамай", "хуами"]


@labeler.chat_message(AliasRule(ALIASES))
@error_handler.catch
async def whoami_handler(message: Message):
    repo = UserRepository(user_id=message.from_id, chat_id=message.chat_id)
    user_info = await repo.get_user()
    response = "Модератор" if user_info.is_moder else "Пользователь"
    return await message.reply(response)
