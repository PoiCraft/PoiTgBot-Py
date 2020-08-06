from command.bind import BindHandler
from command.hitokoto import HitokotoHandler
from command.addWhiteList import addWhiteListHandler
from command.removeWhiteList import removeWhiteListHandler


def add_handler(dispatcher):
    dispatcher.add_handler(HitokotoHandler)
    dispatcher.add_handler(addWhiteListHandler)
    dispatcher.add_handler(BindHandler)
    dispatcher.add_handler(removeWhiteListHandler)
