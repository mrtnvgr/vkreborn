import os

from loguru import logger
from vkbottle import User
from vkbottle.tools.dev.loop_wrapper import LoopWrapper

from vkreborn.config import VKTOKEN
from vkreborn.database.initialize import setup_db
from vkreborn.handlers import labelers
from vkreborn.middlewares import middlewares
from vkreborn.response_validator import CaptchaResponseValidator


@logger.catch
def main():
    os.chdir(os.path.dirname(__file__))

    loop_wrapper = LoopWrapper(on_startup=[setup_db()])
    user = User(VKTOKEN, loop_wrapper=loop_wrapper)

    user.labeler.vbml_ignore_case = True

    for labeler in labelers:
        user.labeler.load(labeler)

    for middleware in middlewares:
        user.labeler.message_view.register_middleware(middleware)

    user.api.response_validators.insert(1, CaptchaResponseValidator())

    user.run_forever()


if __name__ == "__main__":
    main()
