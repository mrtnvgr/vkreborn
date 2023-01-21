from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.error_handler import error_handler
from vkreborn.tools import get_attachments, download_attachment
from shazamio import Shazam

SUPPORTED_ATTACHMENTS = ["audio", "audio_message"]


@labeler.message(
    text="<_:prefix>shazam", attachment=SUPPORTED_ATTACHMENTS, blocking=False
)
@error_handler.catch
async def shazam_attachment_handler(message: Message):
    attachments = await get_attachments(message, SUPPORTED_ATTACHMENTS)
    return await shazam_func(message, attachments)


async def shazam_func(message: Message, attachments: list):

    shazam = Shazam()

    response = []

    for attachment in attachments:

        data = await download_attachment(attachment)

        shazam_response: str = await shazam.recognize_song(data)

        response.append(await format_data(shazam_response))

    if response:
        return await message.reply("\n".join(response))


async def format_data(resp: dict):
    try:
        track = resp["track"]
        return f"{track['subtitle']} - {track['title']}"
    except KeyError:
        return "Ошибка"
