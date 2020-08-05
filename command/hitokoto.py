import json

import requests
from telegram.ext import CommandHandler


def Hitokoto(update, context):
    text = requests.get('https://v1.hitokoto.cn/?c=a')
    content = json.loads(text.text)
    if content['from_who'] is None:
        ret = content['hitokoto'] + '\n---' + ' ' + content['from']
    else:
        ret = content['hitokoto'] + '\n---' + content['from_who'] + ' ' + content['from']
    context.bot.send_message(chat_id=update.effective_chat.id, text=ret, reply_to_message_id=update.message.message_id)


HitokotoHandler = CommandHandler('yy', Hitokoto)
