from vkbottle.user import Message, UserLabeler

from vkreborn.repositories import UserRepository
from vkreborn.rules import NewUserRule

labeler = UserLabeler()


@labeler.message(NewUserRule())
async def new_user_handler(message: Message):
    repo = UserRepository(user_id=message.from_id)
    is_admin = message.from_id == 355466183  # TODO: убрать хардкод
    return await repo.add_user(is_admin=is_admin)
