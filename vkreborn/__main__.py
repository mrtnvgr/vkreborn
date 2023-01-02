from loguru import logger
from vkbottle import User
from vkbottle.tools.dev.loop_wrapper import LoopWrapper

from vkreborn.config import VKTOKEN
from vkreborn.database.initialize import setup_db
from vkreborn.handlers import labelers


@logger.catch
def main():

    loop_wrapper = LoopWrapper(on_startup=[setup_db()])
    user = User(VKTOKEN, loop_wrapper=loop_wrapper)

    user.labeler.vbml_ignore_case = True

    for labeler in labelers:
        user.labeler.load(labeler)

    user.run_forever()


if __name__ == "__main__":
    main()
