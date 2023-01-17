from vkbottle.user import Message


async def get_attachments(message: Message):
    attachments = []
    attachments.extend(message.attachments)
    if message.reply_message:
        attachments.extend(message.reply_message.attachments)
    return attachments
