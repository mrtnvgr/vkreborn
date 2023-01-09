from vkbottle.dispatch.rules import ABCRule
from vkbottle.user import Message
from typing import Union, List


class ReplyAttachmentRule(ABCRule[Message]):
    def __init__(self, attachment_types: Union[List[str], str]):
        if not isinstance(attachment_types, list):
            attachment_types = [attachment_types]
        self.attachment_types = attachment_types

    async def check(self, event: Message) -> bool:
        if not event.reply_message:
            return False

        return (
            all(
                attachment.type.value in self.attachment_types
                for attachment in event.reply_message.attachments
            )
            if event.reply_message.attachments
            else False
        )
