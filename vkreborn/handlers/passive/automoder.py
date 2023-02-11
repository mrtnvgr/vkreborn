from vkbottle.framework.labeler.user import RawUserEvent
from vkbottle_types.events.enums import UserEventType

from vkreborn.error_handler import error_handler
from vkreborn.repositories import UserRepository
from vkreborn.vkbottle import labeler


@labeler.raw_event(UserEventType.CHAT_INFO_EDIT, dataclass=RawUserEvent)
@error_handler.catch
async def automoder_handler(event: RawUserEvent):
    repo = UserRepository(user_id=event.object[3], chat_id=event.object[2])
    value = False if event.object[1] == 9 else True
    await repo.set_moder(value)
