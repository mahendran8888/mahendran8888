from breeze_connect import BreezeConnect
from datetime import datetime,date,time,timedelta
import pandas as pd
import numpy as np

# Allows for printing the whole data frame
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

breeze = BreezeConnect(api_key="83&2~83Y22K2018511yE&w60N2814B97")
breeze.generate_session(api_secret="a68(7S85P4u$568491O#08374w0(6m6d", session_token="1547413")

bnce = breeze.get_historical_data(interval="1minute", from_date="2022-08-20T07:00:00.000Z",
                                       to_date="2022-08-25T18:00:00.000Z", stock_code="CNXBAN", exchange_code="NFO",
                                       product_type="options",expiry_date="2022-09-01T18:00:00.000Z",
                                       right="call",strike_price=40000)
# print(bnce['Success'])
dfbnce = pd.DataFrame(bnce['Success'])
# print(df)
# bnhistory = breeze.get_historical_data(interval="1minute",
#                                        from_date="2022-8-10T07:00:00.000Z",
#                                        to_date="2022-8-10T18:00:00.000Z",
#                                        stock_code="CANBAN",
#                                        exchange_code="NSE",
#                                        product_type="others")

def ATR(DF, n):
    df = DF.copy()
    df['H-L'] = abs(df['high'].astype(float) - df['low'].astype(float))
    df['H-PC'] = abs(df['high'].astype(float) - df['close'].astype(float).shift(1))# high -previous close
    df['L-PC'] = abs(df['low'].astype(float) - df['close'].astype(float).shift(1)) #low - previous close
    df['TR'] = df[['H-L','H-PC','L-PC']].max(axis =1, skipna = False) # True range
    df['ATR'] = df['TR'].rolling(50).mean() # average –true range
        # df['Bricks'] = round(df["ATR"].iloc[-1])
    df = df.drop(['H-L','H-PC','L-PC'], axis =1) # dropping the unneccesary columns
    df.dropna(inplace = True) # droping null items


bricks = round(ATR(dfbnce, 50)["ATR"][-1], 0)
print(bricks)
# print(df.iloc[:,-8:])

















# # print(bnhistory)
# sma = pd.DataFrame(bnhistory['Success'])
# # print(sma.head())
# sma['sma_20'] = sma['close'].rolling(10).mean()
#
# trade_log = pd.DataFrame(columns='Stockcode,strike_price,call, Entry Time, Entry Price, Exit Time, Exit Price'.split(','))
# long_trade_triggered = 0
# for index, row in sma[1:].iterrows():
#     previous_row = sma.iloc[index-1]
#     # print(previous_row['sma_20'])
#     # print("Prev SMA",previous_row['sma_20'],"Prev_row",previous_row['close'],"row:", row['close'],"SMA",row['sma_20'])
#     # if (pd.to_numeric(previous_row['close']) < previous_row['sma_20']) & (pd.to_numeric(row['close']) > row['sma_20']) & (long_trade_triggered == 0):
#     if (pd.to_numeric(previous_row['low']) < previous_row['sma_20']) & (pd.to_numeric(row['low']) > row['sma_20']) & (long_trade_triggered == 0):
#         long_trade_triggered = 1
#         take_profit = pd.to_numeric(row['close'])*0.01 + pd.to_numeric(row['close'])
#         # print("Buy", row['close'],row['datetime'],index)
#         trade_log = trade_log.append({'Stockcode':row['stock_code'],'strike_price':row['strike_price'],'Call':'Buy', 'Entry Time':row['datetime'],'Entry Price' : row['close']},ignore_index=True)
#     elif (long_trade_triggered == 1) &  (pd.to_numeric(previous_row['high']) > previous_row['sma_20']) & (pd.to_numeric(row['high']) < row['sma_20']):
#         # print("Exit", row['close'],row['datetime'],index)
#         long_trade_triggered = 0
#         trade_log = trade_log.append({'Exit Time' :row['datetime'],'Exit Price' : row['close']},ignore_index=True)
# #
# trade_log['Exit Time'] = trade_log['Exit Time'].shift(-1)
# trade_log['Exit Price'] = trade_log['Exit Price'].shift(-1)
# trade_log['PnL'] = pd.to_numeric(trade_log['Exit Price'])- pd.to_numeric(trade_log['Entry Price'])
# trade_log.dropna(how='all', axis=1, inplace=True)
# trade_log.dropna(inplace=True)
# trade_log.reset_index(drop=True, inplace=True)
# print(trade_log)
# print(take_profit, row['close'])
# trade_log.to_csv('C:\\Users\\mahen\\OneDrive\\Desktop\\backtest.csv')


