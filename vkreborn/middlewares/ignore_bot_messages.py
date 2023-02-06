from vkbottle import BaseMiddleware
from vkbottle.user import Message


class IgnoreBotMessagesMiddleware(BaseMiddleware[Message]):
    async def pre(self):
        if self.event.get_payload_json() == {"ignore": "me"}:
            self.stop("Ignoring as requested...")
