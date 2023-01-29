from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import MutedUserRepository
from vkreborn.vkbottle import labeler


@labeler.chat_message(text="<_:prefix>muted")
@labeler.chat_message(text="<_:prefix>мутед")
@labeler.chat_message(text="<_:prefix>мьютед")
@labeler.chat_message(text="<_:prefix>мутэд")
@labeler.chat_message(text="<_:prefix>мьютэд")
@labeler.chat_message(text="<_:prefix>inmute")
@labeler.chat_message(text="<_:prefix>вмуте")
@labeler.chat_message(text="<_:prefix>вмьюте")
@labeler.chat_message(text="<_:prefix>замученые")
@labeler.chat_message(text="<_:prefix>замученные")
@labeler.chat_message(text="<_:prefix>замьюченые")
@labeler.chat_message(text="<_:prefix>замьюченные")
@error_handler.catch
async def muted_here_handler(message: Message):
    repo = MutedUserRepository(muted_where=message.chat_id)
    ids = await repo.list_by_muted_where()

    if len(ids) == 0:
        return

    users = await message.ctx_api.users.get(ids, fields=["domain"])

    text = ["В муте:"]

    for user in users:
        text.append(f"{user.first_name} {user.last_name} ({user.domain})")

    return await message.reply("\n".join(text))
