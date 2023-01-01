import os

from loguru import logger
from vkbottle import Bot

from .handlers import labelers


@logger.catch
def main():
    bot = Bot(os.environ["VKTOKEN"])

    for labeler in labelers:
        bot.labeler.load(labeler)

    bot.run_forever()


if __name__ == "__main__":
    main()
