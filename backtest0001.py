from breeze_connect import BreezeConnect
from datetime import datetime,date,time,timedelta
import pandas as pd
import numpy as np

Login details here
# bnhistory = breeze.get_historical_data(interval="1minute", from_date="2022-08-01T07:00:00.000Z",
#                                        to_date="2022-08-05T18:00:00.000Z", stock_code="CNXBAN", exchange_code="NFO",
#                                        product_type="options",expiry_date="2022-08-11T18:00:00.000Z",
#                                        right="call",strike_price=38600)
bnhistory = breeze.get_historical_data(interval="1minute",
                                       from_date="2022-8-17T07:00:00.000Z",
                                       to_date="2022-8-17T18:00:00.000Z",
                                       stock_code="CANBAN",
                                       exchange_code="NSE",
                                       product_type="others")
sma = pd.DataFrame(bnhistory['Success'])
sma['sma_20'] = sma['close'].rolling(20).mean()



print(sma)


























# def call(x):
#     if x['sma_20'] < pd.to_numeric(x['low']):
#         return 'Buy'
#     elif x['sma_20'] > pd.to_numeric(x['high']):
#         return 'Sell'
#     else:
#         return ' '
# sma['call'] = sma.apply(call, axis=1)
