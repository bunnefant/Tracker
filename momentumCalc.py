import pandas as pd






# calculate all the support and resistance lines based off of the day befores data
def intialResistanceCalc(symbol, DATA_LIST):
    df = DATA_LIST.get(symbol)



# update support and resistances after each min
def minuteUpdate(DATA_LIST):

def marketOpen(DATA_LIST):



def processNewData(DATA_LIST):



def momentumTrack(symbol, DATA_LIST):
    # add math stuff here for momentum track which will be called in mainMarket
    lastThreeCandles = [DATA_LIST.get(symbol).iloc[-1], DATA_LIST.get(symbol).iloc[-2], DATA_LIST.get(symbol).iloc[-3]]
    # if 3 candles result in net positive growth esp if pos, neg, pos and 3rd is higher than closing then hard buy
    # if 3rd candle is very large growth, check net growth in next 2 mins, if pos buy, if not hold off
