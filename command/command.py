from command.addWhiteList import addWhiteListHandler
from command.bind import BindHandler
from command.hitokoto import HitokotoHandler
from command.id import GetIDHandler
from command.removeWhiteList import removeWhiteListHandler
from command.rtp import rtpHandler
from command.team_commands import teamButtonHandler, createTeamHandler, recruitHandler,quitTeamHandler


def add_handler(dispatcher):
    dispatcher.add_handler(HitokotoHandler)
    dispatcher.add_handler(addWhiteListHandler)
    dispatcher.add_handler(BindHandler)
    dispatcher.add_handler(removeWhiteListHandler)
    dispatcher.add_handler(GetIDHandler)
    dispatcher.add_handler(rtpHandler)
    dispatcher.add_handler(teamButtonHandler)
    dispatcher.add_handler(createTeamHandler)
    dispatcher.add_handler(recruitHandler)
    dispatcher.add_handler(quitTeamHandler)
