from vkbottle.user import Message
from vkbottle import AudioUploader
from vkreborn.vkbottle import labeler
from vkreborn.error_handler import error_handler
from vkreborn.tools import get_attachments, download_attachment
from vkreborn.thirdparty import ffmpeg


@labeler.message(
    text="<_:prefix>nc <speed:float>",
    attachment=["audio", "audio_message"],
    blocking=False,
)
@error_handler.catch
async def nc_handler(message: Message, speed: float):
    return await make(message, core=speed)


async def make(message: Message, **fx):

    attachments = get_attachments(message)

    new_attachments = []

    for attachment in attachments:

        content = await download_attachment(attachment)

        new_content = await ffmpeg(content, **fx)

        new_attachment = await AudioUploader(message.ctx_api).upload(
            "PLACEHOLDER ARTIST", "PLACEHOLDER TITLE", new_content
        )
        new_attachments.append(new_attachment)

    return await message.reply(attachments=new_attachments)
