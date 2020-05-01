import os
import requests
import json
import pandas as pd
import csv


BASE_URL = 'https://cloud.iexapis.com/stable'
TEST_API_TOKEN = '?token=sk_df49e6caa5424c16bf0dd9e6eac9435d'


def getQuote(symbol):
    r = requests.get(BASE_URL + '/stock/' + symbol + '/quote' + TEST_API_TOKEN)

    return json.loads(r.content)

def getIntraDay(symbol):
    r = requests.get(BASE_URL + '/stock/' + symbol + '/intraday-prices' + TEST_API_TOKEN)
    #bro = json.loads(r.content)
    #with open('hello.json', 'w') as json_file:
        #json.dump(bro, json_file)
    #out_file = open("hello.json", "w")
    #json.dump(bro, out_file, indent = 6)
    #out_file.close()
    return json.loads(r.content)

def JSONtoCSV(jsonObj):
    df = pd.read_json(jsonObj)
    #df.to_csv(r'C:\Users\bunne\Desktop\stock')


def createCSV():
    with open('C:/users/bunne/desktop/stock/bruh.csv', 'w', newline='') as file:
        data = getIntraDay('AAL')
        writer = csv.writer(file)
        writer.writerow(["Time", "High", "Low", "Open", "Close", "Volume"])
        for x in data:
            writer.writerow([x.get('minute'), x.get('high'), x.get('low'), x.get('open'), x.get('close'), x.get('volume')])

print(getIntraDay('AAL')[0])
createCSV()
