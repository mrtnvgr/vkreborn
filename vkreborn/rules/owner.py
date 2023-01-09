from vkbottle.dispatch.rules import ABCRule
from vkbottle.user import Message


class OwnerRule(ABCRule[Message]):
    def __init__(self, is_owner: bool = True):
        self.is_owner = is_owner

    async def check(self, message: Message):
        account = await message.ctx_api.users.get()
        is_owner = message.from_id == account[0].id
        return self.is_owner is is_owner
