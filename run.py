import logging
from telegram.ext import CommandHandler
import key
from telegram.ext import Updater

updater = Updater(token=key.token, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def yy(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='test')


start_handler = CommandHandler('yy', yy)
dispatcher.add_handler(start_handler)
updater.idle()

updater.stop()
