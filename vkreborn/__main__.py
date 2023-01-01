
import os

from vkbottle import Bot

from .handlers import labelers


if __name__ == "__main__":

    bot = Bot(os.environ["VKTOKEN"])

    for labeler in labelers:
        bot.labeler.load(labeler)

    bot.run_forever()
