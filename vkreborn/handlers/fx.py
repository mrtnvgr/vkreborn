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
    return await make(message, speed=speed)


async def make(message: Message, **fx):

    attachments = await get_attachments(message)

    new_attachments = []

    for attachment in attachments:

        content = await download_attachment(attachment)
        title = await get_audio_title(attachment)

        new_content = await ffmpeg.apply_fx(content, **fx)

        new_title = await ffmpeg.make_title(title, **fx)

        new_attachment = await AudioUploader(message.ctx_api).upload(
            "vkr @p13d3z", new_title, new_content
        )
        new_attachments.append(new_attachment)

    return await message.reply(attachment=new_attachments)


async def get_audio_title(attachment) -> str:
    if attachment.audio:
        return "PLACEHOLDER"

    elif attachment.audio_message:
        # TODO: vkbottle_types#39
        # if attachment.audio_message.transcript:
        #     return attachment.audio_message.transcript
        return "Голосовое сообщение"
