from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import UserRepository
from vkreborn.vkbottle import labeler


@labeler.message(new_user=True)
@error_handler.catch
async def new_user_handler(message: Message):
    account = await message.ctx_api.users.get()
    repo = UserRepository(user_id=message.from_id, chat_id=message.chat_id)
    is_moder = repo.user_id == account[0].id
    await repo.add_user(is_moder=is_moder)
