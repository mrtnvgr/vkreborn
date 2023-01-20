from vkbottle.user import Message
from vkbottle import VKAPIError
from vkreborn.vkbottle import labeler
from vkreborn.repositories import UserRepository
from vkreborn.error_handler import error_handler


@labeler.chat_message(text="<_:prefix>kick <user:mention>", moder=True)
@error_handler.catch
async def kick_handler(message: Message, user: dict):
    kick_resp = await kick(message=message, user=user)
    if not kick_resp:
        return kick_resp
    await message.reply(f"Пользователь {user['domain']} исключен")


@labeler.chat_message(text="<_:prefix>invite <user:mention>", moder=True)
@error_handler.catch
async def invite_handler(message: Message, user: dict):
    await invite(message=message, user_id=user["id"])
    return await message.reply(f"Пользователь {user['domain']} приглашен")


@labeler.chat_message(text="<_:prefix>forceinvite <user:mention>", moder=True)
@error_handler.catch
async def forceinvite_handler(message: Message, user: dict):
    await kick(message=message, user_id=user["id"])
    await invite(message=message, user_id=user["id"])


async def kick(message: Message, user: dict):
    repo = UserRepository(user_id=user["id"], chat_id=message.chat_id)

    moders = await repo.get_moder_ids()
    if repo.user_id in moders:
        await message.reply("Модератора нельзя исключить из беседы")
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
