from breeze_connect import BreezeConnect
from datetime import datetime,date,time,timedelta
import pandas as pd
import numpy as np
import pandas_ta as ta

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

breeze = BreezeConnect(api_key="5x5553j2952i5rde763r4p5)s71I~f63")
breeze.generate_session(api_secret="l5t641026v7EA992c9B4432(05714V62", session_token="1573073")

stock = breeze.get_historical_data(interval="1minute",
                                       from_date="2022-8-29T07:00:00.000Z",
                                       to_date="2022-8-30T18:00:00.000Z",
                                       stock_code="TCS",
                                       exchange_code="NSE",
                                       product_type="others")
df = pd.DataFrame(stock['Success'])
# df.drop([['exchange_code','product_type','expiry_date','right','open_interest','count']], inplace=True, axis=1)
# df["RSI"] = ta.rsi(close = pd.to_numeric(df.close), length=10)
# df['ATR'] = ta.atr(pd.to_numeric(df["high"]),pd.to_numeric(df["low"]),pd.to_numeric(df["close"].shift()), length=14)

high_low = pd.to_numeric(df["high"]) - pd.to_numeric(df["low"])
high_close = np.abs(pd.to_numeric(df["high"]) - pd.to_numeric(df["close"].shift()))
low_close = np.abs(pd.to_numeric(df["low"]) - pd.to_numeric(df["close"].shift()))
ranges = pd.concat([high_low, high_close, low_close], axis=1)
true_range = np.max(ranges, axis=1)
df['ATR'] = true_range.rolling(14).sum()/14

print(df)

