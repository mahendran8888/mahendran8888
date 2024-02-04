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


bnce = breeze.get_historical_data(interval="1minute", from_date="2024-1-19T09:00:00.000Z",
                                       to_date="2024-1-19T18:00:00.000Z", stock_code="CNXBAN", exchange_code="NFO",
                                       product_type="options",expiry_date="2024-1-25T18:00:00.000Z",
                                       right="call",strike_price=47000)
# bnce = breeze.get_historical_data(interval="1minute",
#                                        from_date="2022-9-2T07:00:00.000Z",
#                                        to_date="2022-9-2T18:00:00.000Z",
#                                        stock_code="ITC",
#                                        exchange_code="NSE",
#                                        product_type="others")
# # print(bnhistory)
dfbnce = pd.DataFrame(bnce['Success'])
# print(dfbnce)
# dfbnce['O-C'] = dfbnce['close'].astype(float) - dfbnce['open'].astype(float)
# dfbnce['O-C (0)'] = dfbnce['close'].shift(0).astype(float) - dfbnce['open'].shift(0).astype(float)
# dfbnce['O-C (1)'] = dfbnce['close'].shift(1).astype(float) - dfbnce['open'].shift(1).astype(float)
# dfbnce['O-C (2)'] = dfbnce['close'].shift(2).astype(float) - dfbnce['open'].shift(2).astype(float)
# dfbnce['O-C (3)'] = dfbnce['close'].shift(3).astype(float) - dfbnce['open'].shift(3).astype(float)
# dfbnce['O-C (4)'] = dfbnce['close'].shift(4).astype(float) - dfbnce['open'].shift(4).astype(float)
# dfbnce['O-C (5)'] = dfbnce['close'].shift(5).astype(float) - dfbnce['open'].shift(5).astype(float)
# dfbnce['O-C (6)'] = dfbnce['close'].shift(6).astype(float) - dfbnce['open'].shift(6).astype(float)
# dfbnce['O-C (7)'] = dfbnce['close'].shift(7).astype(float) - dfbnce['open'].shift(7).astype(float)

# dfbnce['o0'] = dfbnce['open'].astype(float).shift(0)
# dfbnce['h0'] = dfbnce['high'].astype(float).shift(0)
# dfbnce['l0'] = dfbnce['low'].astype(float).shift(0)
# dfbnce['c0'] = dfbnce['close'].astype(float).shift(0)

# dfbnce['o1'] = dfbnce['open'].astype(float).shift(1)
# dfbnce['h1'] = dfbnce['high'].astype(float).shift(1)
# dfbnce['l1'] = dfbnce['low'].astype(float).shift(1)
# dfbnce['c1'] = dfbnce['close'].astype(float).shift(1)

# dfbnce['o2'] = dfbnce['open'].astype(float).shift(2)
# dfbnce['h2'] = dfbnce['high'].astype(float).shift(2)
# dfbnce['l2'] = dfbnce['low'].astype(float).shift(2)
# dfbnce['c2'] = dfbnce['close'].astype(float).shift(2)
#
# dfbnce['o3'] = dfbnce['open'].astype(float).shift(3)
# dfbnce['h3'] = dfbnce['high'].astype(float).shift(3)
# dfbnce['l3'] = dfbnce['low'].astype(float).shift(3)
# dfbnce['c3'] = dfbnce['close'].astype(float).shift(3)
#
# dfbnce['o4'] = dfbnce['open'].astype(float).shift(4)
# dfbnce['h4'] = dfbnce['high'].astype(float).shift(4)
# dfbnce['l4'] = dfbnce['low'].astype(float).shift(4)
# dfbnce['c4'] = dfbnce['close'].astype(float).shift(4)
#
# dfbnce['o5'] = dfbnce['open'].astype(float).shift(5)
# dfbnce['h5'] = dfbnce['high'].astype(float).shift(5)
# dfbnce['l5'] = dfbnce['low'].astype(float).shift(5)
# dfbnce['c5'] = dfbnce['close'].astype(float).shift(5)
#
# dfbnce['o6'] = dfbnce['open'].astype(float).shift(6)
# dfbnce['h6'] = dfbnce['high'].astype(float).shift(6)
# dfbnce['l6'] = dfbnce['low'].astype(float).shift(6)
# dfbnce['c6'] = dfbnce['close'].astype(float).shift(6)
#
# dfbnce['o7'] = dfbnce['open'].astype(float).shift(7)
# dfbnce['h7'] = dfbnce['high'].astype(float).shift(7)
# dfbnce['l7'] = dfbnce['low'].astype(float).shift(7)
# dfbnce['c7'] = dfbnce['close'].astype(float).shift(7)

def bull_eng(df):
    df['Bull Engulfing'] = (df['close'].astype(float).shift(0) > df['open'].astype(float).shift(1)) & (df['close'].astype(float).shift(1) > df['open'].astype(float).shift(0))
    return df
# print(bull_eng(dfbnce))

def bear_eng(df):
    df['Bear Engulfing'] = (df['close'].astype(float).shift(0) < df['open'].astype(float).shift(1)) & (df['close'].astype(float).shift(1) < df['open'].astype(float).shift(0))
    return df
# print(bear_eng(dfbnce))

# dfbnce.loc[((dfbnce['c0'] > dfbnce['o1']) & (dfbnce['o0'] < dfbnce['c1'])),'Bull Engulfing'] = 'Bull Eng'
# dfbnce.loc[((dfbnce['c0'] < dfbnce['o1']) & (dfbnce['o0'] > dfbnce['c1'])),'Bear Engulfing'] = 'Bear Eng'
# dfbnce['Ratio'] = dfbnce['O-C (0)'] / dfbnce['O-C (1)']
# dfbnce.loc[(dfbnce['O-C (1)'] < 0) & (dfbnce['O-C (0)'] > 0 ) & (dfbnce['O-C (1)'] / dfbnce['O-C (0)'] < -0.25),'Tweezer Top'] = 'Tweez'
# dfbnce.loc[(dfbnce['O-C (2)'] < 0) & (dfbnce['O-C (1)'] < 0) & (dfbnce['O-C (0)'] > 0 ),'Morn Star'] = 'Morn Star'
# dfbnce.loc[((dfbnce['close'] > dfbnce['o1'])),'Engulfing'] = 'Bull'
# print(dfbnce)
#
# dfbnce['Doji'] = dfbnce['O-C (0)'].apply(lambda x: 'Doji' if x == 0 else '')
# dfbnce.loc[(dfbnce['open'].apply(lambda x: float(x))-dfbnce['close'].apply(lambda x: float(x))) == 0, 'Pattern'] = 'Doji'
#

def bullish_engulfing(df):
    O1 = df['open'].astype(float).shift(1)
    C1 = df['close'].astype(float).shift(1)
    C = df['close'].astype(float).shift(0)
    H = df['high'].astype(float).shift(0)
    L = df['low'].astype(float).shift(0)
    C1 = df['close'].astype(float).shift(1)
    O = df['open'].astype(float).shift(0)
    H_L = H-L
    O_C = abs(O-C)
    AVGH10 = df['high'].astype(float).rolling(10).mean()
    AVGL10 = df['low'].astype(float).rolling(10).mean()
    # df['bull_eng'] = (O1 > C1) & (10 * (C - O)) >= (7 * (H - L)) & (C > O1) & (C1 > O) & (10 * (H - L) >= (12 * (AVGH10 - AVGL10)))
    # print(O1, C1, C, H, L, C1, O, AVGH10, AVGL10)
    # df['bull_eng'] = (O1 > C1) & (C > O1) & (C1 > O) & (10*(C - O)) >= (7*(H - L))
    df['Mrbz'] = H_L = O_C & H_L > 3 * (O_C.astype(float).rolling(15).mean()/2)
    # df = df.join(bull_eng)
    return  df
print(bullish_engulfing(dfbnce))