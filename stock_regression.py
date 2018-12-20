import pandas as pd
import requests
import pprint
import math

# Alpha Advantage API Key: NTPHR1WENP1A3M66
response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=compact&symbol=BRK.B&apikey=NTPHR1WENP1A3M66')
database = response.json()
database = database["Time Series (Daily)"] #Taking the data that relates to the stock only

size = len(database.items())

hd = {'open': [], 'high': [], 'low': [], 'close': [], 'HW_PCT': [], 'PCT_change': [], 'volume': []}

for i in sorted(database.items()):
  hd['close'].append(float(i[1]['4. close']))
  hd['open'].append(float(i[1]['1. open']))
  hd['high'].append(float(i[1]['2. high']))
  hd['low'].append(float(i[1]['3. low']))
  hd['volume'].append(float(i[1]['5. volume']))

for j in range(size):
  hd['HW_PCT'].append((hd['high'][j] - hd['low'][j]) / hd['low'][j] * 100.0)
  hd['PCT_change'].append((hd['close'][j] - hd['open'][j]) / hd['open'][j] * 100.0)

data_train = {'Close': hd['close'], 'HW_PCT': hd['HW_PCT'], 'PCT_Change': hd['PCT_change'], 'Volume': hd['volume']}

# Convert data into a pandas dataframe
dt = pd.DataFrame(data=data_train)
dt.fillna(-9999, inplace=True)

forecast_col = 'Close'
forcast_out = int(math.ceil(0.1*len(dt)))