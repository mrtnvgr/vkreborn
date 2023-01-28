import os
from io import BytesIO

import aiofiles
from PIL import Image, ImageDraw, ImageFont, ImageOps
from vkbottle import PhotoMessageUploader
from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.tools import download_attachment, get_attachments
from vkreborn.vkbottle import labeler

SUPPORTED_ATTACHMENTS = ["photo"]
defaults = {"attachment": SUPPORTED_ATTACHMENTS, "blocking": False}


@labeler.message(text="<_:prefix>dm <text:list>", **defaults)
@labeler.message(text="<_:prefix>дм <text:list>", **defaults)
@labeler.message(text="<_:prefix>demotivator <text:list>", **defaults)
@labeler.message(text="<_:prefix>демотиватор <text:list>", **defaults)
@error_handler.catch
async def dm_default_handler(message: Message, text: list):
    text = text[:2]
    return await make(message, *text)


async def make(message: Message, header: str, footer: str = ""):
    attachments = await get_attachments(message, SUPPORTED_ATTACHMENTS)

    new_attachments = []

    for attachment in attachments:
        content = await download_attachment(attachment)
        new_content = await create(content, header, footer)
        new_attachment = await PhotoMessageUploader(message.ctx_api).upload(new_content)
        new_attachments.append(new_attachment)

    return await message.reply(attachment=new_attachments)


async def create(content: bytes, header: str, footer: str):
    # Загружаем шрифт
    font_path = os.path.join("fonts", "times.otf")
    async with aiofiles.open(font_path, mode="rb") as f:
        font_bytes = await f.read()

    # Открываем картинку
    picture = Image.open(BytesIO(content))

    # Добавляем рамки
    picture = await add_frames(picture)

    # Добавляем черный фон
    picture = await add_bg(picture)

    # Вычисляем размеры текста
    font_size = [20 * (min(picture.size) // 100), 15 * (min(picture.size) // 100)]

    # Рисуем текст
    text = await draw_text(header, footer, font_bytes, font_size)

    # Увеличение фона текста
    text = await expand_bg(picture, text)

    # Соединение
    picture = await join(picture, text)

    # Сохраняем
    output = BytesIO()
    picture.save(output, "PNG")
    output.seek(0)
    return output.getvalue()


async def add_frames(picture):
    picture = ImageOps.expand(picture, 5, (0, 0, 0))
    picture = ImageOps.expand(picture, 3, (255, 255, 255))
    return picture


async def add_bg(picture):
    w, h = picture.size
    h_f = 10 * (h // 100)
    new_picture = Image.new("RGB", (w + (h_f * 2), h + h_f), (0, 0, 0))
    new_picture.paste(picture, (h_f, h_f))
    return new_picture


async def draw_text(header: str, footer: str, font_bytes: bytes, font_size: tuple):
    header_text = await _draw_text(header, font_bytes, font_size[0])
    footer_text = await _draw_text(footer, font_bytes, font_size[1])
    return await join_text(header_text, footer_text)


async def join_text(header_text, footer_text):
    header_w, header_h = header_text.size
    footer_w, footer_h = footer_text.size
    w = max(header_w, footer_w)
    h = header_h + footer_h
    text = Image.new("RGB", (w, h), (0, 0, 0))
    text.paste(header_text, ((w - header_w) // 2, 0))
    text.paste(footer_text, ((w - footer_w) // 2, header_h))
    return text


async def expand_bg(picture, text):
    x = min(picture.size)
    w_txt, h_txt = text.size
    w_proc = 25 * (w_txt // 100)
    h_proc = 25 * (h_txt // 100)
    back = Image.new("RGB", (w_txt + (w_proc * 2), h_txt + (h_proc * 2)), (0, 0, 0))
    back.paste(text, (w_proc, h_proc))
    back.thumbnail((x, x))
    return back


async def join(picture, back):
    w_im, h_im = picture.size
    back.thumbnail((min(w_im, h_im), min(w_im, h_im)))
    w_txt, h_txt = back.size
    picture = picture.crop((0, 0, w_im, h_im + h_txt))
    picture.paste(back, ((w_im - w_txt) // 2, h_im))
    return picture


async def _draw_text(
    text: str,
    font_bytes: bytes,
    font_size: int,
    font_add: int = 20,
    main_fill=(0, 0, 0),
    text_fill=(255, 255, 255),
    text_align: str = "center",
):
    # Загружаем шрифт
    font = ImageFont.truetype(BytesIO(font_bytes), font_size)
    # Получаем размеры
    w_txt, h_txt = ImageDraw.Draw(Image.new("RGB", (1, 1))).multiline_textsize(
        text=text, font=font
    )
    # Рисуем фон
    txt = Image.new("RGB", (w_txt, h_txt + font_add), main_fill)
    # Добавляем шрифт на фон
    ImageDraw.Draw(txt).text(
        (0, 0), text=text, font=font, fill=text_fill, align=text_align
    )
    return txt
