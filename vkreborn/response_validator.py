from typing import TYPE_CHECKING, Any, NoReturn, Union
from vkbottle import ABCResponseValidator
from vkreborn.request_rescheduler import CaptchaRequestRescheduler
from loguru import logger

if TYPE_CHECKING:
    from vkbottle.api import ABCAPI, API


class CaptchaResponseValidator(ABCResponseValidator):
    async def validate(
        self,
        method: str,
        data: dict,
        response: Any,
        ctx_api: Union["ABCAPI", "API"],
    ) -> Union[Any, NoReturn]:
        if "error" not in response:
            return response
        if ctx_api.ignore_errors:
            return None
        if response["error"]["error_code"] != 14:
            return response
        logger.info("Captcha catched! Rescheduling event...")
        return await CaptchaRequestRescheduler().reschedule(
            ctx_api, method, data, response
        )
