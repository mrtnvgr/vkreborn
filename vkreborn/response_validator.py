from typing import TYPE_CHECKING, Any, NoReturn, Union

from loguru import logger
from vkbottle import ABCResponseValidator

from vkreborn.request_rescheduler import CaptchaRequestRescheduler

if TYPE_CHECKING:
    from vkbottle.api import ABCAPI, API


class CaptchaResponseValidator(ABCResponseValidator):
    async def validate(
        self,
        method: str,
        data: dict,
        response: Any,
        ctx_api: Union["ABCAPI", "API"],
        delay: int = 2,
    ) -> Union[Any, NoReturn]:
        if "error" not in response:
            return response
        if ctx_api.ignore_errors:
            return None

        error = response["error"]

        if error["error_code"] == 14:
            logger.warning("Captcha catched! Rescheduling event...")
        elif error["error_code"] == 6:
            logger.warning("Too many requests per second catched! Rescheduling event...")
        elif error["error_code"] == 43:
            logger.warning("Messages are temporary unavailable! Rescheduling event (1 min)...")
            delay = 60
        else:
            return response

        return await CaptchaRequestRescheduler(delay).reschedule(ctx_api, method, data, response)
