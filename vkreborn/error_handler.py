from loguru import logger
from vkbottle import ErrorHandler
from vkbottle.user import Message

error_handler = ErrorHandler(redirect_arguments=True)


@error_handler.register_undefined_error_handler
async def undefined_handler(e: BaseException, message: Message, **args):
    try:
        await message.reply("Что-то пошло не так, произошла неожиданная ошибка!")
    finally:
        logger.exception(f"Ошибка у {message.from_id}: {e}")
        logger.error(f"Аргументы: {args}")


# TODO: https://github.com/vkbottle/vkbottle/commit/ed58f58e0247f5c6011f3eb3cd4b1b87c6da7452#comments
