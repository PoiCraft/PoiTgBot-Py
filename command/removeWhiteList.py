from config import SERVER_HOST, CHAT_ID
from websocket import create_connection
from telegram.ext import CommandHandler, CallbackContext
from telegram import Update, Chat, ChatMember
import time

chat = Chat(CHAT_ID, 'group')


def removeWhiteList(update: Update, context: CallbackContext):
    args = context.args
    user = update.effective_user
    if user:
        if chat.get_member(user.id).status == 'creator' or chat.get_member(user.id).status == 'administrator':
            if len(args) != 0:
                try:
                    ws = create_connection(SERVER_HOST)
                except:
                    context.bot.send_message(chat_id=update.effective_chat.id,
                                             text='服务器去火星了,等会儿再试试吧!',
                                             reply_to_message_id=update.effective_message.id)
                ws.send('whitelist remove %s' % args[0])
                time.sleep(0.1)
                result = ws.recv()
                if result == "Player removed from whitelist":
                    context.bot.send_message(
                        chat_id=update.effective_chat.id, text=('%s已经从Poicraft的白名单中消失了呢!' % args[0]),
                        reply_to_message_id=update.effective_message.id)
                else:
                    context.bot.send_message(chat_id=update.effective_chat.id,
                                             text=('Poicraft的白名单并找不到%s呢!' % args[0]),
                                             reply_to_message_id=update.effective_message.id)
            elif len(args) == 0:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='/removeWhiteList后面必须跟上游戏ID嗷，例：/removeWhiteList HelloWorld',
                                         reply_to_message_id=update.effective_message.id)


removeWhiteListHandler = CommandHandler('removeWhiteList', removeWhiteList, allow_edited=False)
