from typing import List, Union

from vkbottle.dispatch.rules import ABCRule
from vkbottle.user import Message

from vkreborn.tools import get_attachments


class AttachmentRule(ABCRule[Message]):
    def __init__(self, attachment_types: Union[List[str], str]):
        if not isinstance(attachment_types, list):
            attachment_types = [attachment_types]
        self.attachment_types = attachment_types

    async def check(self, event: Message) -> bool:
        attachments = await get_attachments(event)

        if not attachments:
            return False

        return any(attachment.type.value in self.attachment_types for attachment in attachments)
