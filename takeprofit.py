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


bnce = breeze.get_historical_data(interval="1minute", from_date="2024-1-8T09:00:00.000Z",
                                       to_date="2024-1-8T18:00:00.000Z", stock_code="CNXBAN", exchange_code="NFO",
                                       product_type="options",expiry_date="2024-1-10T18:00:00.000Z",
                                       right="call",strike_price=47000)
# bnhistory = breeze.get_historical_data(interval="1minute",
#                                        from_date="2022-8-10T07:00:00.000Z",
#                                        to_date="2022-8-10T18:00:00.000Z",
#                                        stock_code="ITC",
#                                        exchange_code="NSE",
#                                        product_type="others")
# # print(bnhistory)
sma = pd.DataFrame(bnce['Success'])
# print(sma.head())
sma['sma'] = sma['close'].rolling(10).mean()
sma['low(-1)'] = sma['low'].shift(1)
sma['high(-1)'] = sma['high'].shift(1)
sma['sma(-1)'] = sma['sma'].shift(1)

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

print(sma[["close","signal","signal price","datetime"]])

# print(sma)
trade_log = pd.DataFrame(columns='Stockcode,strike_price,call, Entry Time, Entry Price, Exit Time, Exit Price, take_profit'.split(','))
long_trade_triggered = 0
take_profit = 0
percentage = 1
for index, row in sma[1:].iterrows():
    previous_row = sma.iloc[index-1]
    # print(previous_row['sma_20'])
    # print("Prev SMA",previous_row['sma_20'],"Prev_row",previous_row['close'],"row:", row['close'],"SMA",row['sma_20'])
    # if (pd.to_numeric(previous_row['close']) < previous_row['sma_20']) & (pd.to_numeric(row['close']) > row['sma_20']) & (long_trade_triggered == 0):
    if (pd.to_numeric(previous_row['low']) < previous_row['sma']) & (pd.to_numeric(row['low']) > row['sma']) & (long_trade_triggered == 0):
        long_trade_triggered = 1
        take_profit = pd.to_numeric(row['close'])*(1 + (percentage/100))

        # print(take_profit)
        # print("Buy", row['close'],row['datetime'],index)
        trade_log = trade_log.append({'Stockcode':row['stock_code'],'strike_price':row['strike_price'],'Call':'Buy', 'Entry Time':row['datetime'],'Entry Price' : row['close']},ignore_index=True)
        # time.sleep(0.1)
    elif (long_trade_triggered == 1) &  (pd.to_numeric(row['close']) > take_profit):
        # print("Exit", row['close'],row['datetime'],index)
        long_trade_triggered = 0
        trade_log = trade_log.append({'Exit Time' :row['datetime'],'Exit Price' : row['close']},ignore_index=True)
        take_profit = 0
        # time.sleep(0.1)
    # if (pd.to_numeric(previous_row['high']) > previous_row['sma_20']) & (pd.to_numeric(row['high']) < row['sma_20']) & (long_trade_triggered == 0):
    #     long_trade_triggered = 2
    #     take_profit = pd.to_numeric(row['close'])*(1 - (percentage/100))
    #
    #     # print(take_profit)
    #     # print("Buy", row['close'],row['datetime'],index)
    #     trade_log = trade_log.append({'Stockcode':row['stock_code'],'strike_price':row['strike_price'],'Call':'Sell', 'Entry Time':row['datetime'],'Entry Price' : row['close']},ignore_index=True)
    # elif (long_trade_triggered == 2) &  (pd.to_numeric(previous_row['close']) < take_profit):
    #     # print("Exit", row['close'],row['datetime'],index)
    #     long_trade_triggered = 0
    #     trade_log = trade_log.append({'Exit Time' :row['datetime'],'Exit Price' : row['close']},ignore_index=True)
    #     take_profit = 0

trade_log['Exit Time'] = trade_log['Exit Time'].shift(-1)
trade_log['Exit Price'] = trade_log['Exit Price'].shift(-1)
trade_log['PnL'] = pd.to_numeric(trade_log['Exit Price'])- pd.to_numeric(trade_log['Entry Price'])
trade_log['take_profit'] = pd.to_numeric(trade_log['Entry Price'])*(percentage/100 + 1)
trade_log['For a Lot'] = pd.to_numeric(trade_log['PnL'])*25
trade_log.dropna(how='all', axis=1, inplace=True)
trade_log.dropna(inplace=True)
trade_log.reset_index(drop=True, inplace=True)
trade_log['Total'] = trade_log['For a Lot'].sum()
print(trade_log)
# trade_log.to_csv('C:\\Users\\mahen\\OneDrive\\Desktop\\takeprofit.csv')