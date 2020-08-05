from command.bind import BindHandler
from command.hitokoto import HitokotoHandler


# from command.addWhiteList import addWhiteListHandler


def add_handler(dispatcher):
    dispatcher.add_handler(HitokotoHandler)
    # dispatcher.add_handler(addWhiteListHandler)
    dispatcher.add_handler(BindHandler)
