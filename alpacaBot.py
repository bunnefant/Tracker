import alpaca_trade_api as tradeapi
import requests
import json
import pandas as pd
import csv
import plotly.graph_objects as go
from matplotlib import pyplot as plt
import time





BASE_URL = 'https://paper-api.alpaca.markets'
API_KEY = 'PKTLTMFZAEDB8GDRDNGU'
SECRET_KEY = '1Ii6wS5d5ItCvcofkvRRT2qnKuMjzzt6rrLjmbAf'
DATA_LIST = {}





api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, 'v2') # or use ENV Vars shown below
account = api.get_account()
#print(api.get_clock())
#
# CREATE METHOD TO INITIALIZE DATA LIST WITH DAY BEFORE DATA
#

def getQuoteMinute(symbol):
    data = api.get_barset(symbol, 'minute', 325)
    x = data[symbol][0]
    avg = (x.h + x.l + x.c)/3
    priceVolume = DATA_LIST.get(symbol)['vwap'] * DATA_LIST.get(symbol)['volume'] + (avg * x.v)
    totalVolume = DATA_LIST.get(symbol)['volume'] + x.v
    vwap = priceVolume/totalVolume
    df = pd.DataFrame([x.t, x.o, x.c, x.h, x.l, x.v, vwap])
    DATA_LIST.get(symbol).append(df)


def createDataFrame(symbol):
    data = api.get_barset(symbol, 'minute', 325)
    pre = []
    totalVolume = 0
    priceVolume = 0

    for x in data['QEP']:
        avg = (x.h + x.l + x.c)/3
        priceVolume = priceVolume + (avg * x.v)
        totalVolume = totalVolume + x.v
        vwap = priceVolume/totalVolume
        print(str(x.h) + " " + str(x.l) + " " + str(x.c) + " " + str(x.t) + " " + str(x.v) + " " + str(vwap))
        pre.append([x.t,x.o,x.c,x.h,x.l,x.v,vwap])
    df = pd.DataFrame(pre,columns = ['time', 'open', 'close', 'high', 'low', 'volume', 'vwap'])
    DATA_LIST.append(symbol : df)
    return df

def getCurrentTime():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time

def momentumTrack():
    print(getCurrentTime())
    min = 30
    while(True):
        if int(getCurrentTime()[3:5]) == min:
            print('make api call')
            min += 1


        time.sleep(1)
        print("Current Time =", getCurrentTime())


momentumTrack()


#print(api.get_barset('AAL', 'minute', 390))
# DATA_LIST.append(createDataFrame())
# print(DATA_LIST[0])
#
# x = DATA_LIST[0]['time']
# y = DATA_LIST[0]['vwap']
#
# fig = go.Figure(data=[go.Candlestick(x=DATA_LIST[0]['time'],
#                 open=DATA_LIST[0]['open'], high=DATA_LIST[0]['high'],
#                 low=DATA_LIST[0]['low'], close=DATA_LIST[0]['close'])
#                      ])
#
# fig.update_layout(xaxis_rangeslider_visible=False)
# fig.show()
# plt.plot(x,y)
# plt.show()
