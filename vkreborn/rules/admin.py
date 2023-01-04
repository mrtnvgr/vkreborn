from vkbottle.dispatch.rules import ABCRule
from vkbottle.user import Message

from vkreborn.repositories import UserRepository


class AdminRule(ABCRule[Message]):
    def __init__(self, is_admin: bool = True):
        self.is_admin = is_admin

    async def check(self, message: Message):
        repo = UserRepository(user_id=message.from_id, chat_id=message.chat_id)
        user = await repo.get_user()
        return self.is_admin is (user.is_admin is not None)
