from vkbottle.user import Message
from vkbottle import VKAPIError
from vkreborn.vkbottle import labeler
from vkreborn.repositories import UserRepository
from vkreborn.error_handler import error_handler


@labeler.chat_message(text="<_:prefix>kick <user:mention>", admin=True)
@error_handler.catch
async def kick_handler(message: Message, user: dict):
    kick_resp = await kick(message=message, user=user)
    if not kick_resp:
        return kick_resp
    await message.reply(f"Пользователь {user['domain']} был исключен из этой беседы")


@labeler.chat_message(text="<_:prefix>invite <user:mention>", admin=True)
@error_handler.catch
async def invite_handler(message: Message, user: dict):
    await invite(message=message, user_id=user["id"])
    return await message.reply(f"Пользователь {user['domain']} был приглашен в беседу")


@labeler.chat_message(text="<_:prefix>forceinvite <user:mention>", admin=True)
@error_handler.catch
async def forceinvite_handler(message: Message, user: dict):
    await kick(message=message, user_id=user["id"])
    await invite(message=message, user_id=user["id"])


async def kick(message: Message, user: dict):
    repo = UserRepository(user_id=user["id"], chat_id=message.chat_id)

    admins = await repo.get_admin_ids()
    if repo.user_id in admins:
        await message.reply("Администратора нельзя исключить из беседы")
        return False

    try:
        await message.ctx_api.messages.remove_chat_user(
            chat_id=message.chat_id, user_id=user["id"]
        )
    except VKAPIError[935]:
        await message.reply(f"Пользователь {user['domain']} не состоит в беседе")
        return False


async def invite(message: Message, user_id: int, visible_messages_count: int = 250):
    await message.ctx_api.messages.add_chat_user(
        chat_id=message.chat_id,
        user_id=user_id,
        visible_messages_count=visible_messages_count,
    )