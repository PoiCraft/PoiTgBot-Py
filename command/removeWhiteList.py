from telegram import Update, Chat
from telegram.ext import CommandHandler, CallbackContext

from config import TELEGRAM_CHAT_ID,ADMINS_LIST
from control.command import sendCommand

chat = Chat(TELEGRAM_CHAT_ID, 'group')


def removeWhiteList(update: Update, context: CallbackContext):
    args = context.args
    user = update.message.from_user
    if user:
        if user.id in ADMINS_LIST:
            if len(args) != 0:
                res = sendCommand('whitelist remove %s' % args[0], '1')
                if not res.status:
                    context.bot.send_message(chat_id=update.effective_chat.id,
                                             text='服务器去火星了,等会儿再试试吧! 错误信息:' % res.msg,
                                             reply_to_message_id=update.effective_message.id)

                if res.content[0] == "Player removed from whitelist":
                    context.bot.send_message(
                        chat_id=update.effective_chat.id, text=('%s已经从PoiCraft的白名单中消失了呢!' % args[0]),
                        reply_to_message_id=update.effective_message.id)
                else:
                    context.bot.send_message(chat_id=update.effective_chat.id,
                                             text=('PoiCraft的白名单并找不到%s呢!' % args[0]),
                                             reply_to_message_id=update.effective_message.id)
            elif len(args) == 0:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='/removeWhiteList后面必须跟上游戏ID嗷，例：/removeWhiteList HelloWorld',
                                         reply_to_message_id=update.effective_message.id)


removeWhiteListHandler = CommandHandler('removeWhiteList', removeWhiteList)
