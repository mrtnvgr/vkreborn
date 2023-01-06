from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.repositories import UserRepository
from vkreborn.error_handler import error_handler


@labeler.message(text="<_:prefix>admins")
@error_handler.catch
async def admins_handler(message: Message):
    repo = UserRepository(user_id=message.from_id, chat_id=message.chat_id)
    admin_ids = await repo.get_admin_ids()

    admins_info = await message.ctx_api.users.get(admin_ids, fields=["domain"])

    admins = [
        f"{admin.first_name} {admin.last_name} ({admin.domain})"
        for admin in admins_info
    ]
    admins.insert(0, "Администраторы:" if len(admins) > 1 else "Администратор:")

    return await message.reply("\n".join(admins))
