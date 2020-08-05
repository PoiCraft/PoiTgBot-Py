import requests
import json
from telegram.ext import CommandHandler


def Hitokoto(update, context):
    ret = requests.get('https://v1.hitokoto.cn/?c=a')
    data = json.loads(ret.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=ret.text)


HitokotoHandler = CommandHandler('yy', Hitokoto)
