import logging

from telegram.ext import Updater

from command import command
from config import BOT_TOKEN, REQUEST_KWARGS
from control.websocket import createConnection

updater = Updater(token=BOT_TOKEN, use_context=True, request_kwargs=REQUEST_KWARGS)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

command.add_handler(dispatcher)
createConnection()
print('Running...')
updater.start_polling()
updater.idle()
