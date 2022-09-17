from breeze_connect import BreezeConnect
from datetime import datetime, date, time, timedelta
import pandas as pd
import numpy as np

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

breeze = BreezeConnect(api_key="635G46S5M930Z12~n5070z026q8`38C3")
breeze.generate_session(api_secret="40!jl30_255q271c586A)Q9P640869Y7", session_token="1561768")

bnhistory = breeze.get_historical_data(interval="1minute", from_date="2022-08-26T07:00:00.000Z",
                                       to_date="2022-08-26T18:00:00.000Z", stock_code="CNXBAN", exchange_code="NFO",
                                       product_type="options", expiry_date="2022-09-01T18:00:00.000Z",
                                       right="call", strike_price=39600)

# Get quotes of mentioned stock-code
# print(breeze.get_quotes(stock_code="ICIBAN",
#                     exchange_code="NSE",
#                     expiry_date="2022-08-25T06:00:00.000Z",
#                     product_type="cash",
#                     right="others",
#                     strike_price="0")['Success'])

sma = pd.DataFrame(bnhistory['Success'])
sma['sma'] = sma['close'].rolling(10).mean()
# print(sma)
# sma.to_csv('C:\\Users\\mahen\\OneDrive\\Desktop\\Test12345.csv')
print(sma[["stock_code", "open", "high", "low", "close", "sma"]].tail(2))

low = sma['low'].iloc[-1]
lowp = sma['low'].iloc[-2]
high = sma['high'].iloc[-1]
highp = sma['high'].iloc[-2]
close = sma['close'].iloc[-1]
# print(sma)
sma20 = sma['sma'].iloc[-1]
sma20p = sma['sma'].iloc[-2]
print(sma20, sma20p, low, lowp, high, highp)
if sma20 < pd.to_numeric(low) and sma20p > pd.to_numeric(lowp):
    print("Buy at", close)

if sma20 < pd.to_numeric(low) and sma20p > pd.to_numeric(lowp):
    print("Sell at", close)