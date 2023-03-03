import re

from vkbottle import VideoUploader
from vkbottle.http import AiohttpClient
from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.vbml.patcher import TT_URL_RE
from vkreborn.vkbottle import labeler

ALIASES = ["tiktok", "tt", "тикток", "тт"]


@labeler.message(AliasRule(ALIASES, "<url:tt_url>"))
@error_handler.catch
async def tiktok_handler(message: Message, url: str):
    attachment = await download(message=message, url=url)
    if attachment:
        return await message.reply(attachment=attachment)


@labeler.message(AliasRule(ALIASES), reply=True)
@error_handler.catch
async def tiktok_reply_handler(message: Message):
    pattern = re.compile(TT_URL_RE, re.IGNORECASE)
    matches = set(re.findall(pattern, message.reply_message.text))

    if not matches:
        return

    attachments = [
        await download(message=message, url=match, errors=False) for match in matches if match
    ]

    return await message.reply(attachment=attachments)


async def download(message: Message, url: str, errors: bool = True):
    resp = await AiohttpClient().request_json(f"https://tikwm.com/api?url={url}")

    if resp.get("code") == -1:
        if errors:
            await message.reply("Неправильная ссылка")
        return

    video_url = resp["data"]["play"]
    video_bytes = await AiohttpClient().request_content(video_url)

    author = resp["data"]["author"]
    video_author = f'{author["nickname"]} (@{author["unique_id"]})'

    video_title = resp["data"]["title"]
    video_name = f" - {video_title}" if video_title else ""

    requester = await message.reply_message.get_user(fields=["domain"])
    description = ["(This video was uploaded automatically via vkr)"]
    description.append(f"Requested by: @{requester.domain}")

    return await VideoUploader(message.ctx_api).upload(
        video_bytes,
        name=f"{video_author}{video_name}",
        description="\n".join(description),
        is_private=True,
    )
