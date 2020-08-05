from command.hitokoto import HitokotoHandler


def add_handler(dispatcher):
    dispatcher.add_handler(HitokotoHandler)