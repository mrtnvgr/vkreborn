from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import DupeChatRepository
from vkreborn.vkbottle import labeler


@labeler.chat_message(text="<_:prefix>dupeadd <group>", owner=True)
@labeler.chat_message(text="<_:prefix>dupeon <group>", owner=True)
@labeler.chat_message(text="<_:prefix>dupeenable <group>", owner=True)
@labeler.chat_message(text="<_:prefix>dupeset <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпадд <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпад <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпон <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпенабле <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпенейбл <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпенабл <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпэнабле <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпэнейбл <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпэнабл <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпэнэйбл <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеадд <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеад <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеон <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеенабле <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеенейбл <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеенабл <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеэнабле <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеэнейбл <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеэнабл <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеэнэйбл <group>", owner=True)
@error_handler.catch
async def dupeon_handler(message: Message, group: str):
    repo = DupeChatRepository(chat_id=message.chat_id, group=group)

    if await repo.check_group():
        return await message.reply("Текущий чат уже находится в этой дюп-группе")

    await repo.add()

    return await message.reply(f'Текущий чат теперь в дюп-группе "{group}"')
