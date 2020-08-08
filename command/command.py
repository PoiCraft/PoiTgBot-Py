from command.addWhiteList import addWhiteListHandler
from command.bind import BindHandler
from command.hitokoto import HitokotoHandler
from command.id import GetIDHandler
from command.removeWhiteList import removeWhiteListHandler
from command.rtp import rtpHandler
from command.team_commands import team_button_handler, createTeamHandler, recruitHandler


def add_handler(dispatcher):
    dispatcher.add_handler(HitokotoHandler)
    dispatcher.add_handler(addWhiteListHandler)
    dispatcher.add_handler(BindHandler)
    dispatcher.add_handler(removeWhiteListHandler)
    dispatcher.add_handler(GetIDHandler)
    dispatcher.add_handler(rtpHandler)
    dispatcher.add_handler(team_button_handler)
    dispatcher.add_handler(createTeamHandler)
    dispatcher.add_handler(recruitHandler)
