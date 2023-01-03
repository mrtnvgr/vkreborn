from vkbottle.bot import Message
from vkbottle.dispatch.rules import ABCRule

from vkreborn.repositories.user import UserRepository


class NewUserRule(ABCRule[Message]):
    async def check(self, message: Message):
        repo = UserRepository(user_id=message.from_id)
        return await repo.get_user() is None
