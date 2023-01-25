from subprocess import check_output

from vkbottle import AudioUploader
from vkbottle.user import Message

from vkreborn.thirdparty.sox.effects import BaseEffect
from vkreborn.tools import download_attachment, get_attachments

SUPPORTED_ATTACHMENTS = ["audio", "audio_message"]


async def make(message: Message, *fx: list[BaseEffect]):
    attachments = await get_attachments(message, SUPPORTED_ATTACHMENTS)

    new_attachments = []

    for attachment in attachments:

        content = await download_attachment(attachment)
        title = await get_audio_title(attachment)

        new_content = await apply_fx(content, *fx)

        new_title = await make_title(title, *fx)

        new_attachment = await AudioUploader(message.ctx_api).upload(
            "vkr", new_title, new_content
        )
        new_attachments.append(new_attachment)

    return await message.reply(attachment=new_attachments)


async def apply_fx(content: bytes, *effects: list[BaseEffect]):
    filters = [effect.filter for effect in effects]
    filters = " ".join(filters).split(" ")
    header = ["sox", "-G", "-t", "mp3", "-", "-t", "mp3", "-"]
    return check_output(header + filters, input=content)


async def make_title(title: str, *effects: list[BaseEffect]):
    effect_names = [effect.fx_name for effect in effects if effect.fx_name]
    return f"{title} +| {', '.join(effect_names)}"


async def get_audio_title(attachment) -> str:
    if attachment.audio:
        return attachment.audio.title

    elif attachment.audio_message:
        # TODO: vkbottle_types#39
        # if attachment.audio_message.transcript:
        #     return attachment.audio_message.transcript
        return "Голосовое сообщение"
