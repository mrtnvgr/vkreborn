from vkbottle.dispatch.rules import ABCRule
from vkbottle.user import Message
from vkreborn.repositories import MutedUserRepository


class MutedRule(ABCRule[Message]):
    def __init__(self, muted: bool = True):
        self.muted = muted

    async def check(self, message: Message):
        repo = MutedUserRepository(user_id=message.from_id, muted_where=message.chat_id)
        user = await repo.get()
        return self.muted is (user is not None)
