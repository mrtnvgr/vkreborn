from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.repositories import UserRepository
from vkreborn.error_handler import error_handler


@labeler.chat_message(text="<_:prefix>takeadmin <user:mention>", admin=True)
@error_handler.catch
async def takeadmin_handler(message: Message, user: dict):
    repo = UserRepository(user_id=user["id"], chat_id=message.chat_id)

    account = await message.ctx_api.users.get()
    if repo.user_id == account[0].id:
        return await message.reply("...")

    admins = await repo.get_admin_ids()
    if repo.user_id not in admins:
        return await message.reply(
            f"Пользователь {user['domain']} не является администратором"
        )

    await repo.set_admin(False)

    return await message.reply(
        f"Пользователь {user['domain']} снят с должности администратора"
    )
