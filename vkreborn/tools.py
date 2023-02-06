from typing import Optional

from vkbottle.http import AiohttpClient
from vkbottle.user import Message
from vkbottle_types.objects import MessagesMessageAttachment, WallWallpostAttachment


async def get_attachments(
    message: Message,
    attachment_types: Optional[list] = None,
    unpack: bool = True,
):
    # NOTE: Check FAQ

    attachments = []

    if message.attachments:
        attachments = message.attachments

    elif message.reply_message and message.reply_message.attachments:
        attachments = message.reply_message.attachments

    elif message.fwd_messages:
        for msg in message.fwd_messages:
            attachments.extend(await get_attachments(msg))

    # Unpack attachments from wallposts
    if unpack:
        attachments = await _convert_wall_attachments(attachments)

    if attachment_types:
        attachments = await cleanup_attachments(attachments, attachment_types)

    return attachments


async def _convert_wall_attachments(attachments: list):
    for attachment in attachments[:]:

        if attachment.wall:
            wall_attachments = attachment.wall.attachments
        elif attachment.wall_reply:
            wall_attachments = attachment.wall_reply.attachments
        else:
            continue

        # Convert WallWallpostAttachment -> MessagesMessageAttachment
        for wall_attach in wall_attachments:
            attach = await _convert_wall_attachment(wall_attach)
            if attach not in attachments:
                attachments.append(attach)

    return attachments


async def _convert_wall_attachment(attachment: WallWallpostAttachment):
    attachment = attachment.__dict__
    attachment_type = attachment["type"].value
    attachment_data = {attachment_type: attachment[attachment_type]}
    return MessagesMessageAttachment(type=attachment_type, **attachment_data)


async def cleanup_attachments(attachments: list, attachment_types: list):
    for attachment in attachments[:]:
        if attachment.type.value not in attachment_types:
            attachments.remove(attachment)
    return attachments


async def get_url_bytes(url: str):
    client = AiohttpClient()
    content = await client.request_content(url)
    return content


async def download_attachment(attachment: MessagesMessageAttachment):
    if attachment.audio:
        link: str = attachment.audio.url
    elif attachment.audio_message:
        link: str = attachment.audio_message.link_mp3
    elif attachment.photo:
        link: str = attachment.photo.sizes[-1].url
    elif attachment.doc:
        link: str = attachment.doc.url
    else:
        raise Exception("NOT SUPPORTED")

    return await get_url_bytes(link)
