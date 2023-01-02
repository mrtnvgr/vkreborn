from vkbottle.user import Message, UserLabeler

from vkreborn.repositories import UserRepository
from vkreborn.rules import NewUserRule

labeler = UserLabeler()


@labeler.message(NewUserRule())
async def new_user_handler(message: Message):
    repo = UserRepository(user_id=message.peer_id)
    return await repo.add_user()
