import random

from loguru import logger
from vkbottle import PhotoMessageUploader
from vkbottle.http import AiohttpClient
from vkbottle.user import Message

from vkreborn.config import WALLHAVEN_API_KEY
from vkreborn.error_handler import error_handler
from vkreborn.repositories import WHPictureRepository
from vkreborn.vkbottle import labeler


@labeler.message(text="<_:prefix>wh", blocking=False)
@error_handler.catch
async def wh_noargs_handler(message: Message):
    return await send_random_single(message)


@labeler.message(text="<_:prefix>wh <q>", blocking=False)
@error_handler.catch
async def wh_query_handler(message: Message, q: str):
    return await send_random_single(message, q=q)


@labeler.message(text="<_:prefix>wh <q> <categories:wh_switches>", blocking=False)
@error_handler.catch
async def wh_query_categories_handler(message: Message, q: str, categories: str):
    return await send_random_single(message, q=q, categories=categories)


@labeler.message(
    text="<_:prefix>wh <q> <categories:wh_switches> <purity:wh_switches>",
    blocking=False,
)
@error_handler.catch
async def wh_query_categories_purity_handler(
    message: Message, q: str, categories: str, purity: str
):
    return await send_random_single(message, q=q, categories=categories, purity=purity)


async def send_random_single(message: Message, **kwargs):
    photo = await get_random_picture(message, **kwargs)
    if not photo:
        return
    attachment = await PhotoMessageUploader(message.ctx_api).upload(
        photo, message.chat_id
    )
    return await message.reply(attachment=attachment)


async def get_random_picture(message: Message, **kwargs):
    search = await wh_search(sorting="random", **kwargs)
    picture = await pick_random_picture(message, search)
    if not picture:
        await message.reply("К сожалению, фотографии по такому запросу закончились")
        return
    await register_picture(message, picture["id"])
    return await AiohttpClient().request_content(picture["path"])


async def pick_random_picture(message: Message, search: list):
    picture = None
    while len(search) > 0:
        picture = random.choice(search)
        search.remove(picture)

        repo = WHPictureRepository(
            picture_id=picture["id"], where_id=message.chat_id, from_id=message.from_id
        )
        if await repo.get():
            picture = None
            break

    return picture


async def register_picture(message: Message, picture_id: int):
    picture = WHPictureRepository(
        picture_id=picture_id, where_id=message.chat_id, from_id=message.from_id
    )
    await picture.create()


async def wh_search(
    q: str = "",
    categories: str = "111",
    purity: str = "100",
    sorting: str = "date_added",
):
    url = "https://wallhaven.cc/api/v1/search"
    client = AiohttpClient()

    payload = {
        "q": q,
        "categories": categories,
        "sorting": sorting,
        "purity": purity,
    }

    if WALLHAVEN_API_KEY:
        payload["apikey"] = WALLHAVEN_API_KEY
    else:
        logger.warning("Please provide your WALLHAVEN_API_KEY in .env file")

    content = await client.request_json(url, params=payload)
    return content["data"]
