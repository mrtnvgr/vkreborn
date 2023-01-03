from vkreborn.middlewares import new_user_middleware

middlewares = {
    new_user_middleware.NewUserMiddleware,
}

__all__ = ["middlewares"]
