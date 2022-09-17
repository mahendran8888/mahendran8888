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
Login details here

stock = breeze.get_historical_data(interval="1minute",
                                       from_date="2022-9-2T07:00:00.000Z",
                                       to_date="2022-9-2T18:00:00.000Z",
                                       stock_code="TCS",
                                       exchange_code="NSE",
                                       product_type="others")
df = pd.DataFrame(stock['Success'])

# mpf.plot(df,type='renko')
# step = 1
# df['first brick'] = math.floor(pd.to_numeric(df['close']).iloc[0]/step)*step
#
# df['brick_calc'] = math.floor((pd.to_numeric(df['close'])- df['first brick']) / step)




# df['diff'] = pd.to_numeric(df['close']) - pd.to_numeric(df['close']).shift()
# bs =0.50
# df['size diff'] = df['diff'].apply(lambda x:bs if (x >= 0 or x >= bs) else -bs if (x <= 0 or x <= -bs) else '')
# df['size diff01'] = df['diff'].apply(lambda x:bs if (x >= bs) else -bs if (x <= -bs) else '')
# df['value'] = pd.to_numeric(df['size diff']).cumsum()
# print(df)

# renko = indicators.Renko(df)
# print(renko)

def bricks_series(df: pd.DataFrame, step=50):
    prices = pd.to_numeric(df['close']) #all closing price
    # print(prices)
    first_brick = math.floor(prices.iloc[0] / step) * step  # first price * bricksize
    # print(first_brick)
    bricks = [first_brick] # first brick
    # print(bricks, bricks[-1])
    # print(step)
    for price in prices: # loop of all closing price
        # print(price, bricks[-1],step, (bricks[-1] + step),((price - bricks[-1]) / step),math.floor((price - bricks[-1]) / step))
        if price > (bricks[-1] + step):
            # print(bricks[-1])
            step_mult = math.floor((price - bricks[-1]) / step) # round down
            # print(step_mult)
            next_bricks = [bricks[-1] + (mult * step) for mult in range(1, step_mult + 1)]
            # print(next_bricks)
            bricks += next_bricks
            # print(bricks)
        elif price < bricks[-1] - step:
            step_mult = math.ceil((bricks[-1] - price) / step)
            next_bricks = [bricks[-1] - (mult * step) for mult in range(1, step_mult + 1)]
            bricks += next_bricks
        else:
            continue
    return bricks
print(bricks_series(df, 1))
# df['renko'] = bricks_series(df, 1)

