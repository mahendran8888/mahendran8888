from breeze_connect import BreezeConnect
from datetime import datetime,date,time,timedelta
import pandas as pd
import numpy as np
import time

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

breeze = BreezeConnect(api_key="635G46S5M930Z12~n5070z026q8`38C3")
breeze.generate_session(api_secret="40!jl30_255q271c586A)Q9P640869Y7", session_token="1561768")


bnce = breeze.get_historical_data(interval="1minute", from_date="2022-08-24T09:00:00.000Z",
                                       to_date="2022-08-25T18:00:00.000Z", stock_code="CNXBAN", exchange_code="NFO",
                                       product_type="options",expiry_date="2022-09-01T18:00:00.000Z",
                                       right="call",strike_price=40300)

# # print(bnhistory)
sma = pd.DataFrame(bnce['Success'])
sma['sma'] = sma['close'].rolling(10).mean()
sma['low(-1)'] = sma['low'].shift(1)
sma['high(-1)'] = sma['high'].shift(1)
sma['sma(-1)'] = sma['sma'].shift(1)
# sma['signal'] = np.where((sma['low'].astype(float) > sma['sma']), 'Buy', '')
# sma['signal'] = np.where((sma['high'].astype(float) < sma['sma']), 'Sell', '')

conditions = [ (sma['sma'] < sma['low'].astype(float)) & (sma['sma(-1)'] > sma['low(-1)'].astype(float)),
               (sma['sma'] > sma['high'].astype(float)) & (sma['sma(-1)'] < sma['high(-1)'].astype(float))
               ]
choices = ['Buy','Sell']
sma['signal'] = np.select(conditions,choices,default='')

conditions = [ (sma['sma'] < sma['low'].astype(float)) & (sma['sma(-1)'] > sma['low(-1)'].astype(float)),
               (sma['sma'] > sma['high'].astype(float)) & (sma['sma(-1)'] < sma['high(-1)'].astype(float))
               ]
choices = [sma['close'],sma['close']]
sma['signal price'] = np.select(conditions,choices,default='')

print(sma[["close","signal","signal price"]])

