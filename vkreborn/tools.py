from vkbottle.user import Message
from vkbottle.http import AiohttpClient
from vkbottle_types.objects import MessagesMessageAttachment
from typing import Optional


async def get_attachments(
    message: Message,
    attachment_types: Optional[list | None] = None,
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
        attachments = await convert_wall_attachments(attachments)

    if attachment_types:
        attachments = await cleanup_attachments(attachments, attachment_types)

    return attachments


async def convert_wall_attachments(attachments: list):
    for attachment in attachments[:]:
        if attachment.wall:
            for wall_attach in attachment.wall.attachments:
                # Convert WallWallpostAttachment -> MessagesMessageAttachment
                wall_attach = wall_attach.__dict__
                wall_attach_type = wall_attach["type"].value
                wall_attach_data = {wall_attach_type: wall_attach[wall_attach_type]}
                attach = MessagesMessageAttachment(
                    type=wall_attach_type, **wall_attach_data
                )
                if attach not in attachments:
                    attachments.append(attach)
    return attachments


async def cleanup_attachments(attachments: list, attachment_types: list):
    for attachment in attachments[:]:
        if attachment.type.value not in attachment_types:
            attachments.remove(attachment)
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
