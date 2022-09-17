from breeze_connect import BreezeConnect
from datetime import datetime,date,time,timedelta
import pandas as pd
import numpy as np
import pandas_ta as ta
from stocktrends import indicators
import math
import mplfinance as mpf


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

breeze = BreezeConnect(api_key="*U33G22B028y36J5yD4C7269W3$V*0Y1")
breeze.generate_session(api_secret="G1V8u*91o8C618581338220604fEp7z6", session_token="1600261")

stock = breeze.get_historical_data(interval="1minute",
                                       from_date="2022-9-2T07:00:00.000Z",
                                       to_date="2022-9-2T18:00:00.000Z",
                                       stock_code="ITC",
                                       exchange_code="NSE",
                                       product_type="others")
df = pd.DataFrame(stock['Success'])