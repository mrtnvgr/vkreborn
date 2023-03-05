import re
from html import unescape
from subprocess import check_output
from typing import Optional

from aiofiles.tempfile import NamedTemporaryFile
from vkbottle import DocMessagesUploader, PhotoMessageUploader, VideoUploader
from vkbottle.http import AiohttpClient
from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.vbml.patcher import REDDIT_URL_RE
from vkreborn.vkbottle import labeler

ALIASES = [
    "reddit",
    "реддит",
    "редит",
    "redditcross",
    "реддиткросс",
    "реддиткрос",
    "реддитсросс",
    "реддитсрос",
    "редиткросс",
    "редиткрос",
    "редитсросс",
    "редитсрос",
    "redditcrosspost",
    "реддиткросспост",
    "реддиткроспост",
    "реддитсросспост",
    "реддитсроспост",
    "редиткросспост",
    "редиткроспост",
    "редитсросспост",
    "редитсроспост",
    "rcp",
    "рсп",
    "рсип",
    "рсипи",
    "рспи",
    "рцп",
    "рцип",
    "рципи",
    "рцпи",
]


@labeler.message(AliasRule(ALIASES, "<url:reddit_post_url>"))
@error_handler.catch
async def reddit_handler(message: Message, url: str):
    await cross_post(message=message, url=url)


@labeler.message(AliasRule(ALIASES), reply=True)
@error_handler.catch
async def reddit_reply_handler(message: Message):
    pattern = re.compile(REDDIT_URL_RE, re.IGNORECASE)
    matches = set(re.findall(pattern, message.reply_message.text))
    for match in matches:
        await cross_post(message=message, url=match)


async def cross_post(message: Message, url: str):
    url = url.split("?")[0].removesuffix("/")
    resp = await AiohttpClient().request_json(f"{url}/.json")

    if "error" in resp:
        return await message.reply(resp.get("message", "Ошибка!"))

    await parse_resp(message=message, resp=resp)


async def parse_resp(message: Message, resp: dict):
    attachments = []
    has_listings = False
    has_post_info = False
    post_info = {"author": None, "subreddit": None, "title": None, "body": None}

    for thing in resp:
        kind = thing.get("kind")

        # Reference:
        #   Listing - list of things
        #   t3 - post media
        #   t1 - post comments

        # Recursively check listings
        if kind == "Listing":
            await parse_resp(message, thing["data"]["children"])
            has_listings = True
            continue

        # Get post title and author
        elif kind == "t3":
            post_info["author"] = thing["data"]["author"]
            post_info["subreddit"] = thing["data"]["subreddit"]
            post_info["title"] = thing["data"]["title"]
            post_info["body"] = thing["data"]["selftext"]
            has_post_info = True

        # Scrape video from t3
        if kind == "t3" and thing["data"]["is_video"]:
            for media_type, media in thing["data"]["media"].items():
                if media_type == "reddit_video":
                    # WARN: is_gif
                    # WARN: over_18
                    video = await _upload_video(
                        message=message,
                        video_url=media["fallback_url"],
                        subreddit=thing["data"]["subreddit"],
                        redditor=thing["data"]["author"],
                        title=thing["data"]["title"],
                    )
                    attachments.append(video)

                else:
                    await message.reply(f"Unsupported video type?: {media_type}")

        # Scrape photo from t3
        elif kind == "t3" and thing["data"]["url"][-3:] in ["png", "jpg"]:
            photo = await _upload_photo(message, thing["data"]["url"])
            attachments.append(photo)

        # Scrape photo gallery from t3
        elif kind == "t3" and thing["data"].get("media_metadata"):
            for photo in thing["data"]["media_metadata"].values():
                if photo["e"] == "Image":
                    best_quality = photo["p"][-1]
                    # Why???
                    photo_url = unescape(best_quality["u"])

                    photo = await _upload_photo(message, photo_url)
                    attachments.append(photo)

                else:
                    await message.reply(f"Unsupported gallery photo type?: {photo['e']}")

        # Scrape gif from t3
        elif kind == "t3" and thing["data"]["url"][-3:] == "gif":
            gif_bytes = await AiohttpClient().request_content(thing["data"]["url"])
            gif = await DocMessagesUploader(message.ctx_api).upload(gif_bytes)
            attachments.append(gif)

        # These "continue" case is here to prevent false positives
        elif kind in ["t3", "t1"]:
            continue

        else:
            await message.reply(f"Unsupported thing kind: {kind}")

    if has_post_info and not has_listings:
        description = await _generate_description(
            message=message,
            desctype="REDDIT CROSSPOST via VKR",
            subreddit=post_info["subreddit"],
            redditor=post_info["author"],
            title=post_info["title"],
            body=post_info["body"],
        )
        await message.reply(description, attachment=attachments, disable_mentions=True)


async def _upload_video(
    message: Message, video_url: str, subreddit: str, redditor: str, title: str
):
    description = await _generate_description(
        message=message,
        desctype="VIDEO FROM REDDIT CROSSPOST via VKR",
        subreddit=subreddit,
        redditor=redditor,
        title=title,
    )

    video_url = video_url.split("?")[0]
    audio_url = f"{'/'.join(video_url.split('/')[:-1])}/DASH_audio.mp4"

    client = AiohttpClient()
    video_bytes = await client.request_content(video_url)
    audio_bytes = await client.request_content(audio_url)

    result_bytes = await _join_video_with_audio(video_bytes, audio_bytes)
    return await VideoUploader(message.ctx_api).upload(
        result_bytes,
        name=f"u/{redditor} - {title}",
        description=description,
        is_private=True,
    )


async def _upload_photo(message: Message, url: str):
    photo_bytes = await AiohttpClient().request_content(url)
    return await PhotoMessageUploader(message.ctx_api).upload(photo_bytes)


async def _join_video_with_audio(video_bytes: bytes, audio_bytes: bytes):
    async with NamedTemporaryFile("wb", suffix=".mp4") as audio_file:
        await audio_file.seek(0)
        await audio_file.write(audio_bytes)
        payload = [
            "ffmpeg",
            "-loglevel",
            "warning",
            "-i",
            "-",
            "-i",
            audio_file.name,
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-f",
            "ismv",  # Safer mp4 (i believe)
            "-",
        ]
        result = check_output(payload, input=video_bytes)
    return result


async def _generate_description(
    message: Message,
    desctype: str,
    subreddit: str,
    redditor: str,
    title: Optional[str] = None,
    body: Optional[str] = None,
):
    user_domain = (await message.get_user(fields=["domain"])).domain
    description = []
    if title:
        description.append(f'"{title}"\n')
    if body:
        description.append(f"\n{body}\n")
    description.append(desctype)
    description.append(f"Originally posted by u/{redditor} on r/{subreddit}")
    description.append(f"Requester: @{user_domain}")
    return "\n".join(description)
