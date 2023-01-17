from vkbottle.user import Message
from vkbottle.http import AiohttpClient


async def get_attachments(message: Message):
    attachments = []
    attachments.extend(message.attachments)
    if message.reply_message:
        attachments.extend(message.reply_message.attachments)
    return attachments


async def get_url_bytes(url: str):
    client = AiohttpClient()
    content = await client.request_content(url)
    return content
