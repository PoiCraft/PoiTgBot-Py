from telegram.ext import CommandHandler, CallbackContext, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from database.database import get_session, Player, Team
from control.team_api import create_team, join_team
from database.player import get_player_by_player_id
from config import TEAM_MEMBER_MAX
import re


def create_new_team(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    session = get_session()
    player = get_player_by_player_id(user_id)
    if player is not None:
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
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='创建队伍失败！您还没有绑定玩家信息。',
                                 reply_to_message_id=update.message.message_id)


def recruit(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    session = get_session()
    leader = session.query(Player).filter(Player.id == user_id).one_or_none()
    if leader is None:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='发起招募失败!您还没有绑定玩家信息。',
                                 reply_to_message_id=update.message.message_id)
        return
    team = session.query(Team).filter(Team.leader_id == user_id).one_or_none()
    if team is None:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='发起招募失败!您不是队长。',
                                 reply_to_message_id=update.message.message_id)
        return
    members = team.members
    keyboard = [InlineKeyboardButton('Join!!!', callback_data=('join'.join(str(team.id))))]
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
                             text=('%s的队伍正在招募(%s/3)，现有成员：\n %s' % leader.xbox_id, str(len(members)), text1),
                             reply_markup=InlineKeyboardMarkup(keyboard))


def join_team_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    team_id = int(re.search(r'[0-9]*', query.data).group())
    session = get_session()
    player = get_player_by_player_id(query.from_user.id)
    team = session.query(Team).filter(Team.id == team_id).one_or_none()
    if player is None:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='加入失败！您未绑定玩家信息。',
                                 reply_to_message_id=update.message.message_id)
        return
    if team is None:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='不存在的队伍！',
                                 reply_to_message_id=update.message.message_id)
        return
    members = team.members
    if len(members) == TEAM_MEMBER_MAX:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='队伍已满！无法加入。',
                                 reply_to_message_id=update.message.message_id)
        return
    player.team_id = team_id
    session.commit()
    members = team.members
    text = ''
    leader = get_player_by_player_id(team.leader_id)
    keyboard = [InlineKeyboardButton('Join!!!', callback_data=('join'.join(str(team.id))))]
    for i in members:
        text.join(i.xbox_id + '\n')
    if len(members) == TEAM_MEMBER_MAX:
        context.bot.edit_message_text(chat_id=query.message.chat_id,
                                      message_id=query.message.message_id,
                                      text=('%s的队伍已满！现有成员：\n%s' % leader.xbox_id, text))
    else:
        context.bot.edit_message_text(chat_id=query.message.chat_id,
                                      message_id=query.message.message_id,
                                      text=('%s的队伍正在招募(%s/3)，现有成员：\n %s' % leader.xbox_id, str(len(members)), text),
                                      reply_markup=InlineKeyboardMarkup(keyboard))


createTeamHandler = CommandHandler('create_new_team', create_new_team)
recruitHandler = CommandHandler('recruit', recruit)
team_button_handler = CallbackQueryHandler(join_team_callback, pattern=r'join[0-9]*')
