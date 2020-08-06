from telegram import Update, Chat
from telegram.ext import CommandHandler, CallbackContext

from config import TELEGRAM_CHAT_ID
from control.command import sendCommand

chat = Chat(TELEGRAM_CHAT_ID, 'group')


def addWhiteList(update: Update, context: CallbackContext):
    args = context.args
    user = update.effective_user()
    if user:
        if chat.get_member(user.id).status == 'creator' or chat.get_member(user.id).status == 'administrator':
            if len(args) != 0:
                res = sendCommand('whitelist add %s' % args[0], '1')
                if not res.status:
                    context.bot.send_message(chat_id=update.effective_chat.id,
                                             text='服务器去火星了,等会儿再试试吧! 错误信息:' % res.msg,
                                             reply_to_message_id=update.effective_message.id)

                if res.content[0] == "Player added to whitelist":
                    context.bot.send_message(
                        chat_id=update.effective_chat.id, text=('已经把%s添加到PoiCraft的白名单中了呢!' % args[0]),
                        reply_to_message_id=update.effective_message.id)
                elif res.content[0] == 'Player already in whitelist':
                    context.bot.send_message(chat_id=update.effective_chat.id,
                                             text=('%s已经在PoiCraft的白名单中了呢!' % args[0]),
                                             reply_to_message_id=update.effective_message.id)
                else:
                    context.bot.send_message(chat_id=update.effective_chat.id,
                                             text='出了点问题?试试提个issues??? 错误信息:' % res.msg,
                                             reply_to_message_id=update.effective_message.id)
            elif len(args) == 0:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='/addWhiteList后面必须跟上游戏ID嗷，例：/addWhiteList HelloWorld',
                                         reply_to_message_id=update.effective_message.id)
            else:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='无法识别的指令，请重新输入，格式:/addWhiteList [username]',
                                         reply_to_message_id=update.effective_message.id)


addWhiteListHandler = CommandHandler('addWhiteList', addWhiteList)
