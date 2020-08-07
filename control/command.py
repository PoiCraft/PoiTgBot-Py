import json
import urllib.parse

import requests

from config import POIMANAGER_API_URL, POIMANAGER_API_TOKEN


def sendCommand(cmd: str, line: str):
    param = {
        'token': POIMANAGER_API_TOKEN,
        'line': line
    }
    ret = requests.get('%s/api/cmd/%s?%s' % (
        POIMANAGER_API_URL,
        urllib.parse.quote(cmd),
        urllib.parse.urlencode(param)
    ))
    ret = json.loads(ret.text)
    if (ret['code'] != 200) or (ret['msg'] != "OK"):
        return {
            'status': False,
            'msg': ret['msg'],
            'content': []
        }
    else:
        return {
            'status': True,
            'msg': ret['msg'],
            'content': ret['content']
        }
