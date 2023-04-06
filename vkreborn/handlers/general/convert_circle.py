from vkbottle import AiohttpClient, VideoUploader
from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.tools import get_attachments
from vkreborn.vkbottle import labeler

ALIASES = [
    "convertcircle",
    "cc",
    "сс",
    "конвертсиркле",
    "конвертсиркл",
    "конвертсеркле",
    "конвертсеркл",
    "конвертсёркле",
    "конвертсёркл",
    "кк",
    "kk",
]

SUPPORTED_ATTACHMENTS = ["video"]
defaults = {"attachment": SUPPORTED_ATTACHMENTS}


@labeler.message(AliasRule(ALIASES), **defaults)
@error_handler.catch
async def convert_circle_handler(message: Message):
    attachments = await get_attachments(message, attachment_types=SUPPORTED_ATTACHMENTS)

    videos = []

    for attachment in attachments:
        video = attachment.video

        if video.width != 480 and video.height != 480:
            continue

        video_url = video.files.mp4_480
        video_bytes = await AiohttpClient().request_content(video_url)

        video = await VideoUploader(message.ctx_api).upload(
            file_source=video_bytes,
            name=video.title,
            description=video.description,
            is_private=True,
        )

        videos.append(video)

    if videos:
        await message.reply(attachment=videos)
