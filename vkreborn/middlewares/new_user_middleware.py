from vkbottle import BaseMiddleware
from vkbottle.user import Message

from vkreborn.repositories import UserRepository


class NewUserMiddleware(BaseMiddleware[Message]):
    async def pre(self):
        repo = UserRepository(user_id=self.event.from_id)
        is_user_new = await repo.get_user() is None

        if is_user_new:
            is_admin = repo.user_id == 355466183
            await repo.add_user(is_admin=is_admin)
