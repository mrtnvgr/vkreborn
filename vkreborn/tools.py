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


async def download_attachment(attachment):
    if attachment.audio:
        link: str = attachment.audio.url
    elif attachment.audio_message:
        link: str = attachment.audio_message.link_mp3
    else:
        raise Exception("NOT SUPPORTED")

    return await get_url_bytes(link)
