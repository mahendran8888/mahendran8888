from breeze_connect import BreezeConnect
from datetime import datetime,date,time,timedelta
import pandas as pd
import numpy as np
import pandas_ta as ta

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

breeze = BreezeConnect(api_key="S71P6931H176G=3#60s&4zbAmZ531730")
breeze.generate_session(api_secret="7062vS^94R16*92%9S2x4X11%wj714#2", session_token="1592984")

stock = breeze.get_historical_data(interval="1minute",
                                       from_date="2022-9-2T07:00:00.000Z",
                                       to_date="2022-9-2T18:00:00.000Z",
                                       stock_code="ITC",
                                       exchange_code="NSE",
                                       product_type="others")
df = pd.DataFrame(stock['Success'])
# df["RSI"] = ta.rsi(close = pd.to_numeric(df.close), length=10)
# df['ATR'] = ta.atr(pd.to_numeric(df["high"]),pd.to_numeric(df["low"]),pd.to_numeric(df["close"].shift()), length=14)

# high_low = pd.to_numeric(df["high"]) - pd.to_numeric(df["low"])
# high_close = np.abs(pd.to_numeric(df["high"]) - pd.to_numeric(df["close"].shift()))
# low_close = np.abs(pd.to_numeric(df["low"]) - pd.to_numeric(df["close"].shift()))
# ranges = pd.concat([high_low, high_close, low_close], axis=1)
# true_range = np.max(ranges, axis=1)
# df['ATR-C'] = true_range.rolling(14).sum()/14
#
# df["high_low"] = pd.to_numeric(df["high"]) - pd.to_numeric(df["low"])
# df["high_close"] = np.abs(pd.to_numeric(df["high"]) - pd.to_numeric(df["close"].shift()))
# df["low_close"] = np.abs(pd.to_numeric(df["low"]) - pd.to_numeric(df["close"].shift()))
# df["Max"] = df[['high_low','high_close','low_close']].max(axis=1)
# df["ATR-CR"] = df["Max"].rolling(14).sum()/14
# print(df)

# Function to calculate average true range
# def ATR(DF, n):
#   df = DF.copy() # making copy of the original dataframe
df['H-L'] = abs(pd.to_numeric(df['high']) - pd.to_numeric(df['low']))
df['H-PC'] = abs(pd.to_numeric(df['high']) - pd.to_numeric(df['close']).shift())# high -previous close
df['L-PC'] = abs(pd.to_numeric(df['low']) - pd.to_numeric(df['close']).shift()) #low - previous close
df['TR'] = df[['H-L','H-PC','L-PC']].max(axis =1, skipna = False) # True range
df['ATR'] = df['TR'].rolling(14).mean() # average –true range
# df = df.drop(['H-L','H-PC','L-PC','TR','count'], axis =1) # dropping the unneccesary columns
#   df.dropna(inplace = True) # droping null items
# df['bricks'] = round(df["ATR"], 0)
  # return df
print(df)


def ATR(DF, n):
    "function to calculate True Range and Average True Range"
    df = DF.copy()
    df['H-L'] = abs(df['High'] - df['Low'])
    df['H-PC'] = abs(df['High'] - df['Adj Close'].shift(1))
    df['L-PC'] = abs(df['Low'] - df['Adj Close'].shift(1))
    df['TR'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1, skipna=False)
    df['ATR'] = df['TR'].rolling(n).mean()
    # df['ATR'] = df['TR'].ewm(span=n,adjust=False,min_periods=n).mean()
    df2 = df.drop(['H-L', 'H-PC', 'L-PC'], axis=1)
    return df2


def slope(ser, n):
    "function to calculate the slope of n consecutive points on a plot"
    slopes = [i * 0 for i in range(n - 1)]
    for i in range(n, len(ser) + 1):
        y = ser[i - n:i]
        x = np.array(range(n))
        y_scaled = (y - y.min()) / (y.max() - y.min())
        x_scaled = (x - x.min()) / (x.max() - x.min())
        x_scaled = sm.add_constant(x_scaled)
        model = sm.OLS(y_scaled, x_scaled)
        results = model.fit()
        slopes.append(results.params[-1])
    slope_angle = (np.rad2deg(np.arctan(np.array(slopes))))
    return np.array(slope_angle)


def renko_DF(DF):
    "function to convert ohlc data into renko bricks"
    df = DF.copy()
    df.reset_index(inplace=True)
    df = df.iloc[:, [0, 1, 2, 3, 4, 5]]
    df.columns = ["date", "open", "high", "low", "close", "volume"]
    df2 = Renko(df)
    df2.brick_size = max(0.5, round(ATR(DF, 120)["ATR"][-1], 0))
    renko_df = df2.get_ohlc_data()
    renko_df["bar_num"] = np.where(renko_df["uptrend"] == True, 1, np.where(renko_df["uptrend"] == False, -1, 0))
    for i in range(1, len(renko_df["bar_num"])):
        if renko_df["bar_num"][i] > 0 and renko_df["bar_num"][i - 1] > 0:
            renko_df["bar_num"][i] += renko_df["bar_num"][i - 1]
        elif renko_df["bar_num"][i] < 0 and renko_df["bar_num"][i - 1] < 0:
            renko_df["bar_num"][i] += renko_df["bar_num"][i - 1]
    renko_df.drop_duplicates(subset="date", keep="last", inplace=True)
    return renko_df


def OBV(DF):
    """function to calculate On Balance Volume"""
    df = DF.copy()
    df['daily_ret'] = df['Adj Close'].pct_change()
    df['direction'] = np.where(df['daily_ret'] >= 0, 1, -1)
    df['direction'][0] = 0
    df['vol_adj'] = df['Volume'] * df['direction']
    df['obv'] = df['vol_adj'].cumsum()
    return df['obv']


def CAGR(DF):
    "function to calculate the Cumulative Annual Growth Rate of a trading strategy"
    df = DF.copy()
    df["cum_return"] = (1 + df["ret"]).cumprod()
    n = len(df) / (252 * 78)
    CAGR = (df["cum_return"].tolist()[-1]) ** (1 / n) - 1
    return CAGR


def volatility(DF):
    "function to calculate annualized volatility of a trading strategy"
    df = DF.copy()
    vol = df["ret"].std() * np.sqrt(252 * 78)
    return vol


def sharpe(DF, rf):
    "function to calculate sharpe ratio ; rf is the risk free rate"
    df = DF.copy()
    sr = (CAGR(df) - rf) / volatility(df)
    return sr


def max_dd(DF):
    "function to calculate max drawdown"
    df = DF.copy()
    df["cum_return"] = (1 + df["ret"]).cumprod()
    df["cum_roll_max"] = df["cum_return"].cummax()
    df["drawdown"] = df["cum_roll_max"] - df["cum_return"]
    df["drawdown_pct"] = df["drawdown"] / df["cum_roll_max"]
    max_dd = df["drawdown_pct"].max()
    return max_dd
