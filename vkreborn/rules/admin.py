from vkbottle.dispatch.rules import ABCRule
from vkbottle.user import Message

from vkreborn.repositories import UserRepository


class AdminRule(ABCRule[Message]):
    async def check(self, message: Message):
        repo = UserRepository(user_id=message.from_id)
        user = await repo.get_user()
        return user.is_admin is not None
