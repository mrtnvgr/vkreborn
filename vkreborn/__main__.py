import os

from loguru import logger
from vkbottle import User

from vkreborn.handlers import labelers


@logger.catch
def main():
    user = User(os.environ["VKTOKEN"])

    user.labeler.vbml_ignore_case = True

    for labeler in labelers:
        user.labeler.load(labeler)

    user.run_forever()


if __name__ == "__main__":
    main()
