from vkbottle import AudioUploader
from vkbottle.user import Message
from vkbottle_types.objects import MessagesMessageAttachment

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.thirdparty.sox import mix_audios
from vkreborn.tools import download_attachment, get_attachments, get_audio_title
from vkreborn.vkbottle import labeler

SUPPORTED_ATTACHMENTS = ["audio", "audio_message"]
ALIASES = ["mix", "микс", "микх"]
defaults = {"attachment": SUPPORTED_ATTACHMENTS}


@labeler.message(AliasRule(ALIASES), **defaults)
@error_handler.catch
async def mix_handler(message: Message):
    attachments = await get_attachments(message, SUPPORTED_ATTACHMENTS)
    downloaded_attachments = [await download_attachment(attachment) for attachment in attachments]
    new_title = await make_title(attachments)
    new_content = await mix_audios(downloaded_attachments)
    uploaded_result = await AudioUploader(message.ctx_api).upload("vkr", new_title, new_content)
    await message.reply(attachment=uploaded_result)


async def make_title(attachments: list[MessagesMessageAttachment]):
    attachment_titles = [f'"{await get_audio_title(attachment)}"' for attachment in attachments]
    return " + ".join(attachment_titles)
