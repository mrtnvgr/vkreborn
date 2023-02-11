from vkbottle.framework.labeler.user import RawUserEvent
from vkbottle_types.events.enums import UserEventType

from vkreborn.error_handler import error_handler
from vkreborn.repositories import UserRepository
from vkreborn.vkbottle import labeler


@labeler.raw_event(UserEventType.CHAT_INFO_EDIT, dataclass=RawUserEvent)
@error_handler.catch
async def automoder_handler(event: RawUserEvent):
    # TODO: check if owner is admin here
    # TODO: check if chat admins can invite people

    chat_id = 2_000_000 - event.object[2]
    repo = UserRepository(user_id=event.object[3], chat_id=chat_id)
    value = False if event.object[1] == 9 else True
    await repo.set_moder(value)
