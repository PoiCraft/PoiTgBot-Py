import requests
import json

def hitikoto():
    text = requests.get('https://v1.hitokoto.cn/?c=a')
    content = json.loads(text.text)
    if content['from_who']==None:
        return content['hitokoto']+'\n---'+' '+content['from']
    return content['hitokoto']+'\n---'+content['from_who']+' '+content['from']
