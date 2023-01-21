from vkbottle.user import Message
from vkbottle.http import AiohttpClient


async def get_attachments(message: Message):
    # NOTE: Check FAQ
    attachments = await _get_attachments(message)
    if attachments:
        return attachments

    if message.fwd_messages:
        attachments = []
        for msg in message.fwd_messages:
            attachments.extend(await _get_attachments(msg))
        return attachments
    return []


async def _get_attachments(message: Message):
    if message.attachments:
        return message.attachments
    if message.reply_message and message.reply_message.attachments:
        return message.reply_message.attachments
    return []


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
