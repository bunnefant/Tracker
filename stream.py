import json
import pandas as pd
from collections import deque
from regressionCalc import *
import websocket
from datetime import datetime
import alpaca_trade_api as tradeapi


STOCK_LIST = ['AAPL', 'TSLA', 'SRNE']
DATA_LIST = {}
BASE_URL = 'https://paper-api.alpaca.markets'
API_KEY = 'PKTLTMFZAEDB8GDRDNGU'
SECRET_KEY = '1Ii6wS5d5ItCvcofkvRRT2qnKuMjzzt6rrLjmbAf'
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, 'v2') # or use ENV Vars shown below

boughtStock = ''
boughtPrice = 0
currentStopLoss = 0


def on_open(ws):
    global STOCK_LIST
    print("opened")
    auth_data = {
        "action": "authenticate",
        "data": {"key_id": API_KEY, "secret_key": SECRET_KEY}
    }
    ws.send(json.dumps(auth_data))
    streams = []
    listen_message = {"action": "listen", "data": {"streams": ["A.TSLA"]}}
    ws.send(json.dumps(listen_message))


def isItBuy(ticker):
    # check buying conditions and return boolean


def on_message(ws, message):
    global DATA_LIST
    print("received a message")
    print(message)
    data = json.loads(message)
    if data.get('stream')[0:3] == 'AM.':
        ticker = data.get('stream')[3:]
        x = message.get('data')
        pre = [[x.s, x.o, x.c, x.h, x.l, x.a, x.av, x.v, x.vw]] #might have to change if its not an object and its a json instead
        df = pd.DataFrame(pre, columns = ['time', 'open', 'close', 'high', 'low', 'average', 'accumulatedVolume', 'volume', 'vwap'])
        DATA_LIST[ticker] = DATA_LIST.get(ticker).append(df, ignore_index = True)
        print(DATA_LIST.get(ticker))
        if int(getCurrentTime()[3:5]) < 33 and int(getCurrentTime()[0:2]) == 9:
            #do nothing
        else:
            if isItBuy(ticker):
                #make market order with stop loss and initial take profit
                #or for now display all that information

def on_close(ws):
    print("closed connection")

def initalize(DATA_LIST, STOCK_LIST):
    for x in STOCK_LIST:
        pre = [[0,0,0,0,0,0,0,0,0]]
        DATA_LIST[x] = pd.DataFrame(pre, columns = ['time', 'open', 'close', 'high', 'low', 'average', 'accumulatedVolume', 'volume', 'vwap'])
        print(DATA_LIST[x])

def getCurrentTime():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time

def waitForMarketOpen():
    while(not api.get_clock().is_open):
        print(getCurrentTime())
        time.sleep(1)

socket = "wss://data.alpaca.markets/stream"


# initalize(DATA_LIST, STOCK_LIST)
# waitForMarketOpen()
# ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
# ws.run_forever()
bruh = 'hello'
print(bruh[2:])
