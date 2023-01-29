from datetime import datetime

from loguru import logger
from vkbottle.exception_factory import VKAPIError
from vkbottle.user import Message

from vkreborn.error_handler import error_handler
from vkreborn.repositories import MutedUserRepository
from vkreborn.vkbottle import labeler


@labeler.chat_message(muted=True)
@error_handler.catch
async def muted_user_handler(message: Message):
    repo = MutedUserRepository(user_id=message.from_id, muted_where=message.chat_id)
    user = await repo.get()
    if user.muted_until < datetime.now():
        return await repo.delete()

    try:
        await message.ctx_api.messages.delete(
            peer_id=message.peer_id,
            cmids=message.conversation_message_id,
            delete_for_all=True,
        )
    except VKAPIError[15] as ex:
        logger.debug(ex.description)
