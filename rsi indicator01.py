from breeze_connect import BreezeConnect
from datetime import datetime,date,time,timedelta
import pandas as pd
import numpy as np
import time
from credentials001 import *

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

breeze = BreezeConnect(api_key=api_key)
breeze.generate_session(api_secret=api_secret, session_token=session_token)


bnce = breeze.get_historical_data(interval="1minute", from_date="2024-1-10T09:00:00.000Z",
                                       to_date="2024-1-10T18:00:00.000Z", stock_code="CNXBAN", exchange_code="NFO",
                                       product_type="options",expiry_date="2024-1-10T18:00:00.000Z",
                                       right="call",strike_price=47000)
# bnce = breeze.get_historical_data(interval="1minute",
#                                        from_date="2022-9-1T07:00:00.000Z",
#                                        to_date="2022-9-1T18:00:00.000Z",
#                                        stock_code="ITC",
#                                        exchange_code="NSE",
#                                        product_type="others")
# # print(bnhistory)
df = pd.DataFrame(bnce['Success'])
def rma(x, n, y0):
    a = (n-1) / n
    ak = a**np.arange(len(x)-1, -1, -1)
    return np.r_[np.full(n, np.nan), y0, np.cumsum(ak * x) / ak / n + y0 * a**np.arange(1, len(x)+1)]
df['change'] = pd.to_numeric(df['close']).diff()
df['gain'] = df.change.mask(df.change < 0, 0.0)
df['loss'] = -df.change.mask(df.change > 0, -0.0)
n = 14
df['avg_gain'] = rma(df.gain[n+1:].to_numpy(), n, np.nansum(df.gain.to_numpy()[:n+1])/n)
df['avg_loss'] = rma(df.loss[n+1:].to_numpy(), n, np.nansum(df.loss.to_numpy()[:n+1])/n)
df['rs'] = df.avg_gain / df.avg_loss
df['rsi_14'] = 100 - (100 / (1 + df.rs))
print(df)
