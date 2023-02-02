from vkbottle import VideoUploader
from vkbottle.http import AiohttpClient
from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.vkbottle import labeler


@labeler.message(text="<_:prefix>tiktok <url:tt_url>")
@labeler.message(text="<_:prefix>tt <url:tt_url>")
@labeler.message(text="<_:prefix>тикток <url:tt_url>")
@labeler.message(text="<_:prefix>тт <url:tt_url>")
@error_handler.catch
async def tiktok_handler(message: Message, url: str):
    resp = await AiohttpClient().request_json(f"https://tikwm.com/api?url={url}")

    if resp.get("code") == -1:
        return await message.reply("Неправильная ссылка")

    video_url = resp["data"]["play"]
    video_bytes = await AiohttpClient().request_content(video_url)

    author = resp["data"]["author"]
    video_author = f'{author["nickname"]} (@{author["unique_id"]})'

    video_title = resp["data"]["title"]
    video_name = f" - {video_title}" if video_title else ""

    attachment = await VideoUploader(message.ctx_api).upload(
        video_bytes,
        name=f"{video_author}{video_name}",
        description="(This video was uploaded automatically via vkr)",
        is_private=True,
    )
    return await message.reply(attachment=attachment)
