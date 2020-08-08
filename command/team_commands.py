from telegram.ext import ConversationHandler, CommandHandler, CallbackContext, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from database.database import get_session, Player, Team
from control.team_api import create_team, join_team
from database.player import get_player_by_player_id
from config import TEAM_MEMBER_MAX


def create_new_team(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    try:
        session = get_session()
        player = get_player_by_player_id(user_id)
        if player.team is None:
            if create_team(player.id)['result']:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='创建队伍成功！请使用/recruit招募成员',
                                         reply_to_message_id=update.message.message_id)
            else:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='创建队伍失败！请联系管理员。',
                                         reply_to_message_id=update.message.message_id)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='创建队伍失败！您已经加入或创建了队伍。',
                                     reply_to_message_id=update.message.message_id)
    except:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='创建队伍失败！您还没有绑定玩家信息。',
                                 reply_to_message_id=update.message.message_id)


def recruit(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    try:
        session = get_session()
        team = session.query(Team).filter(Team.leader_id == user_id).one()
        leader = session.query(Player).filter(Player.id == user_id).one()
        members = team.members
        keyboard = [InlineKeyboardButton('Join!!!', callback_data='join')]
        text1 = ''
        if len(members) < TEAM_MEMBER_MAX:
            if len(members) != 0:
                for i in members:
                    text1.join(i.xbox_id + '\n')
            else:
                text1.join('\n')
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='队伍已满！无法招募新成员。',
                                 reply_to_message_id=update.message.message_id)
            return
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=('%s的队伍正在招募，目前成员：\n %s' % leader.xbox_id, text1),
                                 reply_markup=InlineKeyboardMarkup(keyboard))
    except:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='发起招募失败!您不是队长或您还没有绑定玩家信息。',
                                 reply_to_message_id=update.message.message_id)


def join_team_callback(update:Update,context:CallbackContext):
    query = update.callback_query


createTeamHandler = CommandHandler('create_new_team', create_new_team)
recruitHandler = CommandHandler('recruit', recruit)
