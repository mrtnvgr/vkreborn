from vkbottle import PhotoMessageUploader
from vkbottle.http import AiohttpClient
from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.rules import AliasRule
from vkreborn.vkbottle import labeler

ALIASES = [
    "stablediffusion",
    "стабледифусион",
    "стабледифужин",
    "стабледифужион",
    "стабледиффусион",
    "стабледиффужин",
    "стабледиффужион",
    "стейблдифусион",
    "стейблдифужин",
    "стейблдифужион",
    "стейблдиффусион",
    "стейблдиффужин",
    "стейблдиффужион",
    "стэйблдифусион",
    "стэйблдифужин",
    "стэйблдифужион",
    "стэйблдиффусион",
    "стэйблдиффужин",
    "стэйблдиффужион",
    "sd",
    "сд",
    "эссд",
    "сдэ",
    "эссдэ",
]


@labeler.message(AliasRule(ALIASES, "<prompt>"))
@error_handler.catch
async def stable_diffusion_handler(message: Message, prompt: str):
    await diffuse(message=message, prompt=prompt)


@labeler.message(AliasRule(ALIASES), reply=True)
@error_handler.catch
async def stable_diffusion_reply_handler(message: Message):
    text = message.reply_message.text
    if not text:
        return
    await diffuse(message=message, prompt=text)


async def diffuse(message: Message, prompt: str):
    client = AiohttpClient()
    response = await client.request_json(
        url="https://api.deepai.org/api/stable-diffusion",
        method="POST",
        data={"text": prompt},
        headers={"api-key": "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"},
    )
    content = await client.request_content(response["output_url"])
    photo = await PhotoMessageUploader(message.ctx_api).upload(content)
    await message.reply(attachment=photo)
