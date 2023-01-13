from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.error_handler import error_handler
from vkbottle import PhotoMessageUploader
from vkbottle.http import AiohttpClient
from vkreborn.repositories import WHPictureRepository
import random


@labeler.message(text="<_:prefix>wh", blocking=False)
@error_handler.catch
async def wh_noargs_handler(message: Message):
    photo = await get_random_picture(message)
    attachment = await PhotoMessageUploader(message.ctx_api).upload(
        photo, message.peer_id
    )
    return await message.reply(attachment=attachment)


@labeler.message(text="<_:prefix>wh <q>", blocking=False)
@error_handler.catch
async def wh_query_handler(message: Message, q: str):
    photo = await get_random_picture(message, q=q)
    attachment = await PhotoMessageUploader(message.ctx_api).upload(
        photo, message.peer_id
    )
    return await message.reply(attachment=attachment)


async def get_random_picture(message: Message, **kwargs):
    search = await wh_search(sorting="random", **kwargs)
    picture = random.choice(search)
    await register_picture(message, picture["id"])
    return await AiohttpClient().request_content(picture["path"])


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

    content = await client.request_json(url, params=payload)
    return content["data"]
