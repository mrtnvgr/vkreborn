from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.repositories import UserRepository
from vkreborn.error_handler import error_handler


@labeler.chat_message(text="<_:prefix>kick <user:mention>", admin=True)
@error_handler.catch
async def kick_handler(message: Message, user: dict):
    await kick(message=message, user_id=user["id"])
    return await message.reply(
        f"Пользователь {user['domain']} был исключен из этой беседы!"
    )


async def kick(message: Message, user_id: int):
    repo = UserRepository(user_id=user_id, chat_id=message.chat_id)

    admins = await repo.get_admin_ids()
    if repo.user_id in admins:
        return await message.reply("Администратора нельзя исключить из беседы")

    await message.ctx_api.messages.remove_chat_user(
        chat_id=message.chat_id, user_id=user_id
    )
