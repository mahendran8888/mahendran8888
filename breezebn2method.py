from breeze_connect import BreezeConnect
from datetime import datetime,date,time,timedelta
import pandas as pd
import numpy as np

# login
breeze = BreezeConnect(api_key="F1o2v998H#L444898z5e6ytB492480a&")
breeze.generate_session(api_secret="J72878G2240318h0p161C49t5Z429T07", session_token="1645806")

# get the strike price at the money
bn = breeze.get_quotes(stock_code="CNXBAN",
                       exchange_code="NFO",
                       expiry_date="2022-09-22T06:00:00.000Z",
                       product_type="cash",
                       right="others",
                       strike_price="0")
df = pd.DataFrame(bn['Success'])
actual_ltp = df[df['exchange_code'] == 'NSE']['ltp']

# round strikeprice of atm
rounded_ltp = round(actual_ltp, -2).to_string(index=False)
rounded_ltp = pd.to_numeric(rounded_ltp).astype(int)

# Call - Premium of 100 - Strikeprice
for i in range(rounded_ltp + 500, rounded_ltp + 1000, 100):
    bnc = breeze.get_quotes(stock_code="CNXBAN",
                            exchange_code="NFO",
                            expiry_date="2022-09-22T06:00:00.000Z",
                            product_type="options",
                            right="call",
                            strike_price=i)
    df = pd.DataFrame(bnc)
    df1.append(df)
df1 = pd.concat(df1)
df1['sq.ltp'] = (df1['ltp'] - 100) * (df1['ltp'] - 100)
print(bnc)
strikeprice100 = df1[df1['sq.ltp'] == df1['sq.ltp'].min(), 'strike_price']
print(strikeprice100)

bnhistory = breeze.get_historical_data(interval="1minute", from_date="2022-08-06T07:00:00.000Z", to_date="2022-08-08T18:00:00.000Z", stock_code="CNXBAN", exchange_code="NSE", product_type="options",expiry_date="2022-08-11T18:00:00.000Z",right="call",strike_price=strikeprice100)
bnquote = breeze.get_quotes(stock_code="CNXBAN",exchange_code="NFO",expiry_date="2022-08-11T06:00:00.000Z",product_type="options",right="call",strike_price=strikeprice100)
sma = pd.DataFrame(bnhistory['Success'])
sma['sma_20'] = bnhistory['ltp'].rolling(20).mean()
print(sma['sma_20'])
print(bnquote['low'])
sma20trigger = sma['sma_20'].iloc[-1]
if bnquote['low'] > sma['sma_20']:
    print("Buy")
if bnquote['low'] < sma['sma_20']:
    print("Sell")
