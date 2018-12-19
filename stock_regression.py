import pandas as pd
import requests

# Alpha Advantage API Key: NTPHR1WENP1A3M66
response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=BRK.B&outputsize=compact&apikey=NTPHR1WENP1A3M66')
data = response.json()
data = data["Time Series (Daily)"] #Taking the data that relates to the stock only

print(data["2018-12-19"])