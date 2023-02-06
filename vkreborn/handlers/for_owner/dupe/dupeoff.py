from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import DupeChatRepository
from vkreborn.vkbottle import labeler


@labeler.chat_message(text="<_:prefix>dupedelete", owner=True)
@labeler.chat_message(text="<_:prefix>dupeoff", owner=True)
@labeler.chat_message(text="<_:prefix>dupedisable", owner=True)
@labeler.chat_message(text="<_:prefix>дюпделете", owner=True)
@labeler.chat_message(text="<_:prefix>дюпделет", owner=True)
@labeler.chat_message(text="<_:prefix>дюпделит", owner=True)
@labeler.chat_message(text="<_:prefix>дюпделите", owner=True)
@labeler.chat_message(text="<_:prefix>дюпдилите", owner=True)
@labeler.chat_message(text="<_:prefix>дюпдилит", owner=True)
@labeler.chat_message(text="<_:prefix>дюпофф", owner=True)
@labeler.chat_message(text="<_:prefix>дюпоф", owner=True)
@labeler.chat_message(text="<_:prefix>дюпдизабле", owner=True)
@labeler.chat_message(text="<_:prefix>дюпдезабле", owner=True)
@labeler.chat_message(text="<_:prefix>дюпдезейбл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпдезайбл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеделете", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеделет", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеделит", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеделите", owner=True)
@labeler.chat_message(text="<_:prefix>дюпедилите", owner=True)
@labeler.chat_message(text="<_:prefix>дюпедилит", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеофф", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеоф", owner=True)
@labeler.chat_message(text="<_:prefix>дюпедизабле", owner=True)
@labeler.chat_message(text="<_:prefix>дюпедезабле", owner=True)
@labeler.chat_message(text="<_:prefix>дюпедезейбл", owner=True)
@labeler.chat_message(text="<_:prefix>дюпедезайбл", owner=True)
@error_handler.catch
async def dupeoff_all_handler(message: Message):
    repo = DupeChatRepository(chat_id=message.chat_id)

    if not await repo.get_chat_groups():
        return await message.reply("Текущий чат не состоит дюп-группах")

    await repo.delete_from_all_groups()
    return await message.reply("Текущий чат удален из всех дюп-групп")


@labeler.chat_message(text="<_:prefix>dupedelete <group>", owner=True)
@labeler.chat_message(text="<_:prefix>dupeoff <group>", owner=True)
@labeler.chat_message(text="<_:prefix>dupedisable <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпделете <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпделет <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпделит <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпделите <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпдилите <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпдилит <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпофф <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпоф <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпдизабле <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпдезабле <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпдезейбл <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпдезайбл <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеделете <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеделет <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеделит <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеделите <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпедилите <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпедилит <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеофф <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпеоф <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпедизабле <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпедезабле <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпедезейбл <group>", owner=True)
@labeler.chat_message(text="<_:prefix>дюпедезайбл <group>", owner=True)
@error_handler.catch
async def dupeoff_one_handler(message: Message, group: str):
    repo = DupeChatRepository(chat_id=message.chat_id, group=group)

    if not await repo.check_group():
        return await message.reply(f'Текущий чат не состоит в группе "{group}"')

    await repo.delete_from_group()
    return await message.reply(f'Текущий чат удален из дюп-группы "{group}"')
