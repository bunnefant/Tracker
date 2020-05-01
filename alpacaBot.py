import alpaca_trade_api as tradeapi
import requests
import json
import pandas as pd
import csv
import plotly.graph_objects as go
from matplotlib import pyplot as plt




BASE_URL = 'https://paper-api.alpaca.markets'
API_KEY = 'PKTLTMFZAEDB8GDRDNGU'
SECRET_KEY = '1Ii6wS5d5ItCvcofkvRRT2qnKuMjzzt6rrLjmbAf'

def getQuote(symbol):
    r = requests.get(BASE_URL + '/bars/minute')
    return json.loads(r.content)

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, 'v2') # or use ENV Vars shown below
account = api.get_account()
#print(api.get_clock())


def createCSV():
    with open('C:/users/bunne/desktop/stock/AAL428.csv', 'w', newline='') as file:
        data = api.get_barset('QEP', 'minute', 325)

        #writer = csv.writer(file)
        #writer.writerow(["Time", "High", "Low", "Open", "Close", "Volume"])
        pre = []
        totalVolume = 0
        priceVolume = 0
        y = 0
        for x in data['QEP']:
            #print(x.v)
            #if(y > 60):
                #break;
            avg = (x.h + x.l + x.c)/3
            priceVolume = priceVolume + (avg * x.v)
            totalVolume = totalVolume + x.v
            vwap = priceVolume/totalVolume
            print(str(x.h) + " " + str(x.l) + " " + str(x.c) + " " + str(x.t) + " " + str(x.v) + " " + str(vwap))
            pre.append([x.t,x.o,x.c,x.h,x.l,x.v,vwap])
            y = y + 1
            #print(x)
            #writer.writerow([x.t, x.h, x.l, x.o, x.c, x.v])
        df = pd.DataFrame(pre,columns = ['time', 'open', 'close', 'high', 'low', 'volume', 'vwap'])
        return df
#print(api.get_barset('AAL', 'minute', 390))
df = createCSV()
print(df)

x = df['time']
y = df['vwap']

plt.plot(x,y)
plt.show()

fig = go.Figure(data=[go.Candlestick(x=df['time'],
                open=df['open'], high=df['high'],
                low=df['low'], close=df['close'])
                     ])
#bruh = px.Line(df, x = 'time', y = 'vwap')
#bruh.show()
fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()
