from config import SERVER_HOST
from websocket import create_connection
from telegram.ext import CommandHandler, CallbackContext
from telegram import Update, Chat, ChatMember
import time

chat = Chat('114514', 'group')
ws = create_connection(SERVER_HOST)

#这里不写异步，可以让老板花钱请人优化
def AddWhiteList(update: Update, context: CallbackContext):
    args = context.args
    user = update.effective_user
    if user:
        if chat.get_member(user.id).status == 'creater' or chat.get_member(user.id).status == 'administrator':
            if len(args) != 0:
                ws.send('whitelist add %s' % args[0])
                time.sleep(0.1)
                result = ws.recv()
                if result == "Player added to whitelist":
                    context.bot.send_message(
                        chat_id=update.effective_chat.id, text=('已经把%s添加到Poicraft的白名单中了呢!' % args),
                        reply_to_message_id=update.effective_message.id)
                elif result == 'Player already in whitelist':
                    context.bot.send_message(chat_id=update.effective_chat.id,
                                             text=('%s已经在Poicraft的白名单中了呢!' % args),
                        reply_to_message_id=update.effective_message.id)
                else:
                    context.bot.send_message(chat_id=update.effective_chat.id,
                                             text='出了点问题?试试提个issues???',
                        reply_to_message_id=update.effective_message.id)
            elif len(args) == 0:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='/addWhiteList后面必须跟上游戏ID嗷，例：/addWhiteList HelloWorld',
                                         reply_to_message_id=update.effective_message.id)


addWhiteListHandler = CommandHandler('addWhiteList', AddWhiteList, allow_edited=False)
