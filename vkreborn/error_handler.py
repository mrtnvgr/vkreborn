from loguru import logger
from vkbottle import ErrorHandler
from vkbottle.user import Message

error_handler = ErrorHandler(redirect_arguments=True)


@error_handler.register_undefined_error_handler
async def undefined_handler(e: BaseException, message: Message, **_):
    try:
        await message.reply("Что-то пошло не так, произошла неожиданная ошибка!")
    except Exception as ex:
        logger.error(f"Exception in error_handler: {ex}")
    finally:
        logger.error(f"{message.from_id}: {e}")
