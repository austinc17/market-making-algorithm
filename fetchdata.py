from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime
import pandas as pd

API_KEY = "APIkey"
SECRET_KEY = "Secretkey"

client = StockHistoricalDataClient(API_KEY, SECRET_KEY)

request = StockBarsRequest(
    symbol_or_symbols="AAPL",
    timeframe=TimeFrame.Minute,
    start=datetime(2024, 1, 1),
    end=datetime(2024, 1, 5)
)

bars = client.get_stock_bars(request).df.reset_index()

output = bars[["symbol", "timestamp", "close"]].copy()
output.columns = ["symbol", "timestamp", "price"]

output.to_csv("stockdata/prices.csv", index=False)
print(output.head())
