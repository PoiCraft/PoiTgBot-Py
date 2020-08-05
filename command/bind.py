from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters

from database.database import get_session, Player
from database.player import get_user_by_user_id, get_user_by_xbox_id


def Bind(update, context):
    if get_user_by_user_id(update.effective_user.id) is None:
        context.bot.send_message(chat_id=update.effective_chat.id, text='欢迎绑定账号，请输入您的 XBoxID')
        return 0
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='您已经绑定过账号了哦，请先解绑后再绑定')
        return ConversationHandler.END


def XBoxInput(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="请稍等，我们正在绑定")
    if get_user_by_xbox_id(update.message.text) is None:
        session = get_session()
        session.add(Player(TelegramID=update.effective_user.id, XBoxID=update.message.text, TpNumber=3))
        session.commit()
        session.close()
        context.bot.send_message(chat_id=update.effective_chat.id, text="绑定成功")
        return ConversationHandler.END
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="此账号已经被别人绑定了哦！如果这是你的账号，请联系管理")
        return ConversationHandler.END


def BindCancel(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="绑定请求已被取消")
    return ConversationHandler.END


BindHandler = ConversationHandler(
    entry_points=[CommandHandler('bind', Bind)],
    states={
        0: [MessageHandler(Filters.all, XBoxInput, )]
    },
    fallbacks=[CommandHandler('cancel', BindCancel)]
)
