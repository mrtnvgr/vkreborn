from vkbottle.user import Message
from vkreborn.vkbottle import labeler
from vkreborn.repositories import UserRepository


@labeler.message(new_user=True)
async def new_user_handler(message: Message):
    account = await message.ctx_api.users.get()
    repo = UserRepository(user_id=message.from_id, chat_id=message.chat_id)
    is_admin = repo.user_id == account[0].id
    await repo.add_user(is_admin=is_admin)
