from vkbottle.dispatch.rules import ABCRule
from vkbottle.user import Message


class ReplyMessageRule(ABCRule[Message]):
    def __init__(self, reply_message: bool = True):
        self.reply_message = reply_message

    async def check(self, event: Message) -> bool:
        return self.reply_message is bool(event.reply_message)
