from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.error_handler import error_handler
from vkbottle import PhotoMessageUploader
from vkbottle.http import AiohttpClient
import random


@labeler.message(text="<_:prefix>wh", blocking=False)
@error_handler.catch
async def wh_noargs_handler(message: Message):
    photo = await get_random_picture()
    attachment = await PhotoMessageUploader(message.ctx_api).upload(
        photo, message.peer_id
    )
    return await message.reply(attachment=attachment)


@labeler.message(text="<_:prefix>wh <q>", blocking=False)
@error_handler.catch
async def wh_query_handler(message: Message, q: str):
    photo = await get_random_picture(q=q)
    attachment = await PhotoMessageUploader(message.ctx_api).upload(
        photo, message.peer_id
    )
    return await message.reply(attachment=attachment)


async def get_random_picture(**kwargs):
    seed = random.randint(1, 999999)
    search = await wh_search(seed=seed, **kwargs)
    picture = random.choice(search)["path"]
    return await AiohttpClient().request_content(picture)


async def wh_search(
    q: str = "", categories: str = "111", purity: str = "100", seed: str = ""
):
    url = "https://wallhaven.cc/api/v1/search"
    client = AiohttpClient()

    payload = {
        "q": q,
        "categories": categories,
        "purity": purity,
        "seed": seed,
    }

    content = await client.request_json(url, data=payload)
    return content["data"]
