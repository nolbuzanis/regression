import pandas as pd
import requests
import pprint

# Alpha Advantage API Key: NTPHR1WENP1A3M66
response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=compact&symbol=BRK.B&apikey=NTPHR1WENP1A3M66')
database = response.json()
database = database["Time Series (Daily)"] #Taking the data that relates to the stock only

w = len(database.items())
print w

hd = dict()
hd['open'] = []
hd['high'] = []
hd['low'] = []
hd['close'] = []

for i in sorted(database.items()):
  hd['close'].append(float(i[1]['4. close']))
  hd['open'].append(float(i[1]['1. open']))
  hd['high'].append(float(i[1]['2. high']))
  hd['low'].append(float(i[1]['3. low']))

pprint.pprint(hd)