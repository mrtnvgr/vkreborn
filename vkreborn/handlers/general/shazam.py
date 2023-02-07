from shazamio import Shazam
from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.tools import download_attachment, get_attachments
from vkreborn.vkbottle import labeler

SUPPORTED_ATTACHMENTS = ["audio", "audio_message"]
defaults = {"attachment": SUPPORTED_ATTACHMENTS}


@labeler.message(AliasRule(["shazam", "шазам"]), **defaults)
@error_handler.catch
async def shazam_handler(message: Message):
    attachments = await get_attachments(message, SUPPORTED_ATTACHMENTS)
    return await shazam_func(message, attachments)


async def shazam_func(message: Message, attachments: list):
    shazam = Shazam()

    response = []

    for attachment in attachments:
        data = await download_attachment(attachment)
        shazam_response: str = await shazam.recognize_song(data)
        response.append(await format_data(shazam_response))

    if len(response) > 1:
        response = [f"{str(i+1).zfill(2)} {line}" for i, line in enumerate(response)]

    if response:
        return await message.reply("\n".join(response))


async def format_data(resp: dict):
    try:
        track = resp["track"]
        return f"{track['subtitle']} - {track['title']}"
    except KeyError:
        return "Не найдено!"
