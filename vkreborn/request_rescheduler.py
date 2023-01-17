import asyncio
from typing import TYPE_CHECKING, Any, Union

from vkbottle import ABCRequestRescheduler

if TYPE_CHECKING:
    from vkbottle.api import ABCAPI, API


class CaptchaRequestRescheduler(ABCRequestRescheduler):
    def __init__(self, delay: int = 2):
        self.delay = delay

    async def reschedule(
        self,
        ctx_api: Union["ABCAPI", "API"],
        method: str,
        data: dict,
        recent_response: Any,
    ) -> dict:
        await asyncio.sleep(self.delay)
        return await ctx_api.request(method, data)
