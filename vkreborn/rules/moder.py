from vkbottle.dispatch.rules import ABCRule
from vkbottle.user import Message

from vkreborn.repositories import UserRepository


class ModerRule(ABCRule[Message]):
    def __init__(self, is_moder: bool = True):
        self.is_moder = is_moder

    async def check(self, message: Message):
        repo = UserRepository(user_id=message.from_id, chat_id=message.chat_id)
        user = await repo.get_user()
        return self.is_moder is (user.is_moder is not None)
