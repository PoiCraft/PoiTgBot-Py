from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from control.command import sendCommand
from config import RANDOM_TP
from database.database import get_session, Player
from sqlalchemy.orm.exc import NoResultFound
import random
import time


def rtp(update: Update, context: CallbackContext):
    user = update.message.from_user
    try:
        session = get_session()
        player = session.query(Player).filter(Player.TelegramID == user.id).one()
    except NoResultFound:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="您没有绑定哦~请使用/bind [XboxID]进行绑定",
                                 reply_to_message_id=update.effective_message.id)
    if player.TpNumber < RANDOM_TP:
        res = sendCommand('testfor \"%s\"' % player.XBoxID, '1')
        if not res.status:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='服务器去火星了,等会儿再试试吧! 错误信息:' % res.msg,
                                     reply_to_message_id=update.effective_message.id)
        elif res.content[0] != 'No targets matched selector':
            player.TpNumber += 1
            session.commit()
            session.close()
            x = random.randint(30000, 70000) * -1  # 随机X轴
            z = random.randint(30000, 70000) * -1  # 随机Z轴
            sendCommand('effect \"%s\" resistance 15 5 true' % player.XBoxID, '1')
            time.sleep(0.2)
            sendCommand('tp \"%s\" %s 120 %s' % player.XBoxID, x, z)
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=f'您已被传送至{x},120,{z}\n使用次数:{player.TpNumber}/{RANDOM_TP}\n传送本不易，且行且珍惜',
                                     reply_to_message_id=update.effective_message.id)

        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='您当前不在线上！',
                                     reply_to_message_id=update.effective_message.id)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='今日随机传送次数已用完,且行且珍惜',
                                 reply_to_message_id=update.effective_message.id)


rtpHandler = CommandHandler('rtp', rtp)
