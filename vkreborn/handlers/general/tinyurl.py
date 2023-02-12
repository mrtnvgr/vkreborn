from vkbottle.http import AiohttpClient
from vkbottle.user import Message

from vkreborn.config import TINYURL_API_TOKEN
from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = ["tinyurl", "тинуурл", "тиниурл", "тайниурл"]


@labeler.message(AliasRule(ALIASES, "<url:url>"))
@error_handler.catch
async def tinyurl_handler(message: Message, url: str):
    base_url = "https://api.tinyurl.com/create"

    payload = {
        "url": url,
        "domain": "rotf.lol",
    }

    if TINYURL_API_TOKEN:
        payload["api_token"] = TINYURL_API_TOKEN

    resp = await AiohttpClient().request_json(base_url, method="POST", params=payload)

    if resp["code"] == 0:
        await message.reply(resp["data"]["tiny_url"])
    else:
        await message.reply("\n".join(resp["errors"]))
