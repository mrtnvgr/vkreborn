from vkreborn.middlewares.muted_user import MutedUserMiddleware
from vkreborn.middlewares.new_user import NewUserMiddleware

middlewares = {NewUserMiddleware, MutedUserMiddleware}

__all__ = ["middlewares"]
