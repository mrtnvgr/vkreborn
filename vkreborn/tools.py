from vkbottle.user import Message
from vkbottle.http import AiohttpClient


async def get_attachments(message: Message):
    # NOTE: Check FAQ
    if message.attachments:
        return message.attachments
    if message.reply_message and message.reply_message.attachments:
        return message.reply_message.attachments


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
