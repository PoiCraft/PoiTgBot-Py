import requests
import json


Return = requests.get('https://v1.hitokoto.cn/?c=a')
Json = json.loads(Return.text)
