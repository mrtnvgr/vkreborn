from vkbottle.user import Message
from vkbottle import AudioUploader
from vkreborn.vkbottle import labeler
from vkreborn.error_handler import error_handler
from vkreborn.tools import get_attachments, download_attachment
from vkreborn.thirdparty import ffmpeg
from vkreborn.config import FX_NIGHTCORE_SPEED, FX_DAYCORE_SPEED

defaults = {"attachment": ["audio", "audio_message"], "blocking": False}


@labeler.message(text="<_:prefix>nc <speed:float>", **defaults)
@labeler.message(text="<_:prefix>nightcore <speed:float>", **defaults)
@labeler.message(text="<_:prefix>dc <speed:float>", **defaults)
@labeler.message(text="<_:prefix>daycore <speed:float>", **defaults)
@labeler.message(text="<_:prefix>core <speed:float>", **defaults)
@error_handler.catch
async def core_handler(message: Message, speed: float):
    return await make(message, speed=speed)


@labeler.message(text="<_:prefix>nc", **defaults)
@labeler.message(text="<_:prefix>nightcore", **defaults)
@error_handler.catch
async def nightcore_handler(message: Message):
    return await make(message, speed=FX_NIGHTCORE_SPEED)


@labeler.message(text="<_:prefix>dc", **defaults)
@labeler.message(text="<_:prefix>daycore", **defaults)
@error_handler.catch
async def daycore_handler(message: Message):
    return await make(message, speed=FX_DAYCORE_SPEED)


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
