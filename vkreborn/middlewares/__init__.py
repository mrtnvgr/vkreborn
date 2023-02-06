from vkreborn.middlewares.dupe import DupeMiddleware
from vkreborn.middlewares.ignore_bot_messages import IgnoreBotMessagesMiddleware
from vkreborn.middlewares.muted_user import MutedUserMiddleware
from vkreborn.middlewares.new_user import NewUserMiddleware

middlewares = {
    IgnoreBotMessagesMiddleware,
    NewUserMiddleware,
    MutedUserMiddleware,
    DupeMiddleware,
}

__all__ = ["middlewares"]
