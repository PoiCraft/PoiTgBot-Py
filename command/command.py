from command.bind import BindHandler
from command.hitokoto import HitokotoHandler


def add_handler(dispatcher):
    dispatcher.add_handler(HitokotoHandler)
    dispatcher.add_handler(BindHandler)