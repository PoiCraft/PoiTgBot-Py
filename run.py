import logging
from telegram.ext import Updater
from config import BOT_TOKEN
from command import command

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

command.add_handler(dispatcher)
updater.start_polling()
updater.idle()
