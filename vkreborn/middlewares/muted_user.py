from datetime import datetime

from vkbottle import BaseMiddleware
from vkbottle.exception_factory import VKAPIError
from vkbottle.user import Message

from vkreborn.repositories import MutedUserRepository


class MutedUserMiddleware(BaseMiddleware[Message]):
    async def pre(self):
        repo = MutedUserRepository(user_id=self.event.from_id, muted_where=self.event.chat_id)
        user = await repo.get()

        if user is None:
            return

        if user.muted_until < datetime.now():
            return await repo.delete()

        try:
            await self.event.ctx_api.messages.delete(
                peer_id=self.event.peer_id,
                cmids=self.event.conversation_message_id,
                delete_for_all=True,
            )
            self.stop("User is muted")
        except VKAPIError[924]:
            return await repo.delete()
