from telegram import Update
from telegram.ext import CallbackContext, CommandHandler


def GetID(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='USER ID:%s \nCHAT ID:%s' %
                                  (update.message.from_user.id,
                                   update.message.chat_id),
                             reply_to_message_id=update.message.message_id)


GetIDHandler = CommandHandler('id', GetID)
