import alpaca_trade_api as tradeapi
import requests
import json
import pandas as pd
from collections import deque
from regressionCalc import *

# Streaming imports
import asyncio
import os
import sys
import websocket


from datetime import datetime

from alpaca_trade_api import StreamConn



BASE_URL = 'https://paper-api.alpaca.markets'
API_KEY = 'PKTLTMFZAEDB8GDRDNGU'
SECRET_KEY = '1Ii6wS5d5ItCvcofkvRRT2qnKuMjzzt6rrLjmbAf'
DATA_LIST = {}
STOCK_LIST = ['AAPL']
conn = StreamConn(API_KEY, SECRET_KEY, BASE_URL)




api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, 'v2') # or use ENV Vars shown below
account = api.get_account()
#print(api.get_clock())
#
# CREATE METHOD TO INITIALIZE DATA LIST WITH DAY BEFORE DATA
#

def getQuoteMinute(symbol):
    global DATA_LIST
    data = api.get_barset(symbol, 'minute', 1)
    print(data)
    x = data[symbol][0]
    avg = (x.h + x.l + x.c)/3
    priceVolume = DATA_LIST.get(symbol)[0].vwap.iat[-1] * DATA_LIST.get(symbol)[0]['volume'].sum() + (avg * x.v)
    totalVolume = DATA_LIST.get(symbol)[0]['volume'].sum() + x.v
    vwap = priceVolume/totalVolume
    pre = [[x.t, x.o, x.c, x.h, x.l, x.v, vwap]]
    df = pd.DataFrame(pre,columns = ['time', 'open', 'close', 'high', 'low', 'volume', 'vwap'])
    #print(df)
    #print(DATA_LIST.get(symbol))
    DATA_LIST[symbol] = [DATA_LIST.get(symbol)[0].append(df, ignore_index = True), DATA_LIST.get(symbol)[1], DATA_LIST.get(symbol)[2]]
    #DATA_LIST = DATA_LIST.get(symbol)[0].append(df, ignore_index = True)



# def createDataFrame(symbol):
#     global DATA_LIST
#     data = api.get_barset(symbol, 'minute', 325)
#     pre = []
#     totalVolume = 0
#     priceVolume = 0
#
#     for x in data[symbol]:
#         avg = (x.h + x.l + x.c)/3
#         priceVolume = priceVolume + (avg * x.v)
#         totalVolume = totalVolume + x.v
#         vwap = priceVolume/totalVolume
#         #print(str(x.h) + " " + str(x.l) + " " + str(x.c) + " " + str(x.t) + " " + str(x.v) + " " + str(vwap))
#         pre.append([x.t,x.o,x.c,x.h,x.l,x.v,vwap])
#     df = pd.DataFrame(pre,columns = ['time', 'open', 'close', 'high', 'low', 'volume', 'vwap'])
#     resistanceStack = deque()
#     supportStack = deque()
#     #DATA_LIST = DATA_LIST.update({symbol:[df, resistanceStack, supportStack]})
#     DATA_LIST[symbol] = [df, resistanceStack, supportStack]
#     return df





def getCurrentTime():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time


def mainMarket():
    global DATA_LIST
    #createDataFrame('AAPL')
    while(not api.get_clock().is_open):
        print(getCurrentTime())
        time.sleep(1)
    min = 54
    #INITIALIZE all the stock dataframes for DATA_LIST
    for x in STOCK_LIST:
        createDataFrame(x)
    print(DATA_LIST)
    while(api.get_clock().is_open):
        if int(getCurrentTime()[3:5]) == min:
            #update this minutes stocks
            print(list(DATA_LIST.keys()))
            time.sleep(1)
            for x in list(DATA_LIST.keys()):
                getQuoteMinute(x)
            # Do all the math and stuff and update the DATA_LIST as needed and make calls on should we buy or sell or what
            print(DATA_LIST)
            if min == 59:
                min = 0
            else:
                min = int(getCurrentTime()[3:5]) + 1
            #this is to update the time to make sure we are only making 1 api call per stock per minute
        time.sleep(1) #so our computers dont get destroyed
        print("Current Time =", getCurrentTime())

mainMarket()
# @conn.on(r'^AM$')
# async def on_minute_bars(conn, channel, bar):
#     print('bars', bar)
#     print("Current Time =", getCurrentTime())

# @conn.on(r'^A$')
# async def on_second_bars(conn, channel, bar):
#     print('hello')
#     #print('bars', bar)
#     # ts = int(bar.s)
#     # print(ts)
#     #print("Current Time =", getCurrentTime())
#
# def testStream():
#     global conn
#     print('hello')
#     conn.run(['A.APT'])
#     print('hello')



# mainMarket()
#print(df1)

#print(df1)
#print(DATA_LIST.keys())
#print(DATA_LIST)
#print(nDegreeRegressorTime(df1, 'close', 10, 60))

#print(quadRegressor(df1, 'low'))


# createDataFrame('AAPL')
# createDataFrame('apt')
# print(list(DATA_LIST.keys())[1])
# createDataFrame('AAPL')
# getQuoteMinute('AAPL')
# getQuoteMinute('AAPL')

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
