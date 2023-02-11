from urllib.parse import quote_plus

from vkbottle import PhotoMessageUploader
from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.tools import get_url_bytes
from vkreborn.vkbottle import labeler

ALIASES = [
    "qrcreate",
    "qrmake",
    "qrnew",
    "кьюкреате",
    "кьюкреэйт",
    "кьюаркреате",
    "кьюаркреэйт",
    "куаркреате",
    "куаркреэйт",
    "кркреате",
    "кркреэйт",
    "кьюкрмаке",
    "кьюкрмейк",
    "кьюкрмэйк",
    "куармаке",
    "куармейк",
    "куармэйк",
    "крмаке",
    "крмейк",
    "крмэйк",
    "кьюкрнью",
    "кьюкрнев",
    "куарнью",
    "куарнев",
    "крнью",
    "крнев",
]


@labeler.message(AliasRule(ALIASES, "<data>"))
@error_handler.catch
async def qrcreate_handler(message: Message, data: str):
    base_url = "http://api.qrserver.com/v1/create-qr-code/?data="
    qr = await get_url_bytes(f"{base_url}{quote_plus(data)}")
    photo = await PhotoMessageUploader(message.ctx_api).upload(qr)
    await message.reply(attachment=photo)
