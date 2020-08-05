import logging
from telegram.ext import CommandHandler
import key
import importlib
from telegram.ext import Updater
import Hitokoto

updater = Updater(token=key.token, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def yy(update, context):
    importlib.reload(Hitokoto)
    context.bot.send_message(chat_id=update.effective_chat.id, text=Hitokoto.Return.text)


start_handler = CommandHandler('yy', yy)
dispatcher.add_handler(start_handler)
updater.start_polling()
updater.idle()
