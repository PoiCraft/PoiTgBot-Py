import json

from websocket import create_connection

from config import POIMANAGER_API_WS, POIMANAGER_API_TOKEN

connection = create_connection(POIMANAGER_API_WS)


def createConnection():
    connection.send(json.load({'token': POIMANAGER_API_TOKEN}))
    result = connection.recv()
    res = json.loads(result)
    if (res.type != 'auth') or (res.msg != 'OK') or (res.code != 200):
        print("poimanager auth error:", res.msg)
