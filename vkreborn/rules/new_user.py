from vkbottle.dispatch.rules import ABCRule
from vkbottle.user import Message

from vkreborn.repositories import UserRepository


class NewUserRule(ABCRule[Message]):
    async def check(self, message: Message):
        repo = UserRepository(user_id=message.from_id)
        user = await repo.get_user()
        return user is None
