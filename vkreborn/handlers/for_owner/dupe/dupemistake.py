from vkbottle import VKAPIError
from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import DupeChatRepository, DupeItemRepository
from vkreborn.rules import AliasRule
from vkreborn.tools import get_attachment_hash, get_attachments
from vkreborn.vkbottle import labeler

ALIASES = [
    "dupeerror",
    "дюпееррор",
    "дюперрор",
    "дюпеэррор",
    "дюпэррор",
    "дюпеерр",
    "дюперр",
    "дюпеэрр",
    "дюпэрр",
    "дюпеошибка",
    "дюпошибка",
    "dupemistake",
    "дюпемистаке",
    "дюпмистаке",
    "дюпемистейк",
    "дюпмистейк",
    "dupewrong",
    "дюпевронг",
    "дюпвронг",
    "dupeoops",
    "дюпеоопс",
    "дюпоопс",
    "дюпеупс",
    "дюпупс",
    "дюпеупси",
    "дюпупси",
]


@labeler.chat_message(AliasRule(ALIASES), reply=True, owner=True)
@error_handler.catch
async def dupemistake_handler(message: Message):
    # Получаем группы чата
    chat_repo = DupeChatRepository(chat_id=message.chat_id)
    chat_groups = await chat_repo.get_chat_groups()
    if not chat_groups:
        return await message.reply("Чат не состоит в дюп-группах")

    # Получаем вложения
    attachments = await get_attachments(message)
    if not attachments:
        return

    for attachment in attachments:
        # Получаем хэш вложения
        attachment_hash = await get_attachment_hash(attachment)
        if not attachment_hash:
            attachments.remove(attachment)
            continue

        # Удаляем хэш из БД
        for group in chat_groups:
            item_repo = DupeItemRepository(hash=attachment_hash, group=group)
            await item_repo.delete()

    try:
        await message.ctx_api.messages.delete(
            peer_id=message.reply_message.peer_id,
            cmids=message.reply_message.conversation_message_id,
            delete_for_all=True,
        )
    except VKAPIError:
        await message.reply("Ошибка удаления сообщения")
