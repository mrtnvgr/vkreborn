from vkbottle import BaseMiddleware, VKAPIError
from vkbottle.user import Message
from vkbottle_types.objects import MessagesMessageAttachment

from vkreborn.repositories import DupeChatRepository, DupeItemRepository
from vkreborn.tools import get_attachment_hash, get_old_attachment_hash, get_attachments


class DupeMiddleware(BaseMiddleware[Message]):
    async def post(self):
        # Получаем группы чата
        chat_repo = DupeChatRepository(chat_id=self.event.chat_id)
        chat_groups = await chat_repo.get_chat_groups()
        if not chat_groups:
            return

        # Получаем количество вложений из БД
        none_item_repo = DupeItemRepository()
        individual_counts = await none_item_repo.count_groups(groups=chat_groups)
        summary_count = await none_item_repo.count_all()

        # Итерация через вложения
        attachments = await get_attachments(self.event, reply=False)
        duped_attachments = []
        for attachment in attachments:
            # Удаление старых вложений
            old_hash = await get_old_attachment_hash(attachment)

            if old_hash:
                for group in chat_groups:
                    old_repo = DupeItemRepository(hash=old_hash, group=group)
                    await old_repo.delete()

            # Получаем хэш вложения
            attachment_hash = await get_attachment_hash(attachment)
            if not attachment_hash:
                attachments.remove(attachment)
                continue

            # Проверяем наличие айтема в группах чата
            item_repo = DupeItemRepository(hash=attachment_hash)
            item_groups = await item_repo.get_item_groups()
            if any([item_group in chat_groups for item_group in item_groups]):
                duped_attachments.append(attachment)
            else:
                await item_repo.add_to_groups(groups=chat_groups)

        # Проверяем майлстоуны
        new_individual_counts = await none_item_repo.count_groups(groups=chat_groups)
        await check_for_individual_milestones(
            message=self.event, counts=individual_counts, new_counts=new_individual_counts
        )
        new_summary_count = await none_item_repo.count_all()
        await check_for_summary_milestone(
            message=self.event, count=summary_count, new_count=new_summary_count
        )

        if not duped_attachments:
            return

        try:
            await self.event.ctx_api.messages.delete(
                peer_id=self.event.peer_id,
                cmids=self.event.conversation_message_id,
                delete_for_all=True,
            )
        except VKAPIError:
            word = "Вложение" if len(duped_attachments) == 1 else "Вложения"
            word2 = "дубликат" if len(duped_attachments) == 1 else "дубликаты"
            indexes = [str(attachments.index(attachment) + 1) for attachment in duped_attachments]
            return await self.event.reply(f"{word} {', '.join(indexes)} {word2}")

        new_attachments = [
            get_attachment_string(i) for i in attachments if i not in duped_attachments
        ]
        if new_attachments:
            await self.event.answer(attachment=new_attachments, payload='{"ignore":"me"}')


async def check_for_individual_milestones(
    message: Message, counts: dict[str, int], new_counts: dict[str, int], gap: int = 100
):
    for group in counts.keys():
        count = counts[group]
        new_count = new_counts[group]

        if count // gap < new_count // gap:
            milestone = new_count // gap * gap
            reply = f'🎉 Дюп-группа "{group}" преодолела отметку в {milestone} вложений! 🎉'
            await message.reply(reply)


async def check_for_summary_milestone(
    message: Message, count: int, new_count: int, gap: int = 100
):
    if count // gap < new_count // gap:
        milestone = new_count // gap * gap
        reply = f"🎉 Количество вложений со всех дюп-групп достигло {milestone}! 🎉"
        await message.reply(reply)


def get_attachment_string(attachment: MessagesMessageAttachment):
    attachment_type = attachment.type.value
    attachment_object = getattr(attachment, attachment_type)
    if not hasattr(attachment_object, "id") or not hasattr(attachment_object, "owner_id"):
        raise Exception()
    attachment_string = f"{attachment_type}{attachment_object.owner_id}_{attachment_object.id}"
    if attachment_object.access_key:
        attachment_string += f"_{attachment_object.access_key}"
    return attachment_string
