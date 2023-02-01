from vkbottle import BaseMiddleware
from vkbottle.user import Message

from vkreborn.repositories import UserRepository


class NewUserMiddleware(BaseMiddleware[Message]):
    async def pre(self):
        repo = UserRepository(user_id=self.event.from_id, chat_id=self.event.chat_id)
        user = await repo.get_user()

        if user is None:
            account = await self.event.ctx_api.users.get()
            is_moder = repo.user_id == account[0].id
            await repo.add_user(is_moder=is_moder)
