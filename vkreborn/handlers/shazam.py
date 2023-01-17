from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.error_handler import error_handler
from vkbottle.http import AiohttpClient
from shazamio import Shazam


@labeler.message(
    text="<_:prefix>shazam", attachment=["audio", "audio_message"], blocking=False
)
@error_handler.catch
async def shazam_attachment_handler(message: Message):
    return await shazam_func(message, message.attachments)


async def shazam_func(message: Message, attachments: list):

    shazam = Shazam()

    response = []

    for attachment in attachments:

        if attachment.audio:
            link: str = attachment.audio.url
        elif attachment.audio_message:
            link: str = attachment.audio_message.link_mp3
        else:
            continue

        data: bytes = await get_bytes(link)

        shazam_response: str = await shazam.recognize_song(data)

        response.append(await format_data(shazam_response))

    if response:
        return await message.reply("\n".join(response))


async def get_bytes(url: str):
    client = AiohttpClient()
    content = await client.request_content(url)
    return content


async def format_data(resp: dict):
    try:
        track = resp["track"]
        return f"{track['subtitle']} - {track['title']}"
    except KeyError:
        return "Ошибка"
