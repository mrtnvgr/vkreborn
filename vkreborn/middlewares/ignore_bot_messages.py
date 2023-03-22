from vkbottle import BaseMiddleware
from vkbottle.user import Message


class IgnoreBotMessagesMiddleware(BaseMiddleware[Message]):
    async def pre(self):
        info = await self.event.ctx_api.users.get()
        is_owner = info[0].id == self.event.from_id

        ignore_payload = self.event.get_payload_json() == {"ignore": "me"}

        if is_owner and ignore_payload:
            self.stop("Ignoring as requested...")
