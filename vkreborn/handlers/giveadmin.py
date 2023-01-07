from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.repositories import UserRepository
from vkreborn.error_handler import error_handler


@labeler.chat_message(text="<_:prefix>giveadmin <user:mention>", admin=True)
@error_handler.catch
async def giveadmin_handler(message: Message, user: dict):
    repo = UserRepository(user_id=user["id"], chat_id=message.chat_id)
    await repo.set_admin(True)
    return await message.reply(
        f"Пользователь {user['domain']} теперь админ в этой беседе!"
    )
