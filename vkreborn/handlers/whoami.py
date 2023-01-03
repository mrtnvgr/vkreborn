from vkbottle.user import Message, UserLabeler

from vkreborn.repositories import UserRepository

labeler = UserLabeler()


@labeler.message(command="whoami")
async def new_user_handler(message: Message):
    repo = UserRepository(user_id=message.peer_id)
    user_info = await repo.get_user()
    response = "Админ" if user_info.is_admin else "Пользователь"
    return await message.reply(response)
