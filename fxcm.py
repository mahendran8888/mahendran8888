import fxcmpy
import pandas as pd
import numpy as np
import datetime as dt
from pyti.exponential_moving_average import exponential_moving_average as ema

# Allows for printing the whole data frame
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


TOKEN = "f8ef36fc1e075b614653e2364ee608684b383b7d"
con = fxcmpy.fxcmpy(access_token = TOKEN, log_level = 'error')
# instruments = con.get_instruments()
# print(instruments)

df = con.get_candles('EUR/USD', period='m1',start= dt.datetime(2022, 8, 24),end = dt.datetime(2022, 8, 25))
print(df.head())