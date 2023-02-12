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
    create_func = create_v2_api if TINYURL_API_TOKEN else create_legacy_api
    await create_func(message, url)


async def create_v2_api(message: Message, url: str):
    base_url = "https://api.tinyurl.com/create"

    payload = {
        "url": url,
        "api_token": TINYURL_API_TOKEN,
        "domain": "rotf.lol",
    }

    resp = await AiohttpClient().request_json(base_url, method="POST", params=payload)

    if resp["code"] == 0:
        await message.reply(resp["data"]["tiny_url"])
    else:
        await message.reply("\n".join(resp["errors"]))


async def create_legacy_api(message: Message, url: str):
    base_url = "http://tinyurl.com/api-create.php"
    payload = {"url": url}
    resp = await AiohttpClient().request_text(base_url, params=payload)
    await message.reply(resp)
