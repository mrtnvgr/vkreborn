from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.repositories import UserRepository
from vkreborn.error_handler import error_handler


@labeler.chat_message(text="<_:prefix>givemoder <user:mention>", moder=True)
@error_handler.catch
async def givemoder_handler(message: Message, user: dict):
    repo = UserRepository(user_id=user["id"], chat_id=message.chat_id)

    moders = await repo.get_moder_ids()
    if repo.user_id in moders:
        return await message.reply(
            f"Пользователь {user['domain']} уже является модератором"
        )

    await repo.set_moder(True)

    return await message.reply(
        f"Пользователь {user['domain']} теперь модератор"
    )
