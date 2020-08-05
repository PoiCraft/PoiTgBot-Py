import json
import threading

import websocket

from config import POIMANAGER_API_WS, POIMANAGER_API_TOKEN


class WebSocket:
    def __init__(self):
        self.auth = False
        self.ws = websocket.WebSocketApp(POIMANAGER_API_WS,
                                         on_close=self.on_close,
                                         on_message=self.on_message)
        self.wsthread = None

    def on_open(self, ws):
        self.ws.send(json.load({'token': POIMANAGER_API_TOKEN}))

    def on_message(self, ws, message):
        res = json.loads(message)
        print(res)
        if (res.type == 'auth') and (res.msg == 'OK'):
            self.auth = True
            return

    def on_close(self):
        self.run()

    def run(self):
        self.wsthread = threading.Thread(target=self.ws.run_forever)
        self.wsthread.run()
