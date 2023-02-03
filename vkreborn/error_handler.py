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
