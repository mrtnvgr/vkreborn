from urllib.parse import quote_plus

from vkbottle import AiohttpClient
from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.tools import get_attachments
from vkreborn.vkbottle import labeler

ALIASES = [
    "qrread",
    "кьюкрреад",
    "кьюкррид",
    "кьюарреад",
    "кьюаррид",
    "куарреад",
    "куаррид",
    "крреад",
    "кррид",
]
SUPPORTED_ATTACHMENTS = ["photo"]


@labeler.message(AliasRule(ALIASES), attachment=SUPPORTED_ATTACHMENTS)
@error_handler.catch
async def qrread_handler(message: Message):
    base_url = "http://api.qrserver.com/v1/read-qr-code/?fileurl="
    attachments = await get_attachments(message, SUPPORTED_ATTACHMENTS)
    for attachment in attachments:
        url = attachment.photo.sizes[-1].url
        resp = await AiohttpClient().request_json(f"{base_url}{quote_plus(url)}")
        for item in resp:
            text = [seq["data"] for seq in item["symbol"] if seq["data"]]
            if not text:
                continue
            await message.reply("\n".join(text))
