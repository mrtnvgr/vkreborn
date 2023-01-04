from vkbottle.dispatch.rules import ABCRule
from vkbottle.user import Message

from vkreborn.repositories import UserRepository


class NewUserRule(ABCRule[Message]):
    def __init__(self, _: bool):
        super().__init__()

    async def check(self, message: Message):
        repo = UserRepository(user_id=message.from_id, chat_id=message.chat_id)
        user = await repo.get_user()
        return user is None