from breeze_connect import BreezeConnect
from datetime import datetime,date,time,timedelta
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

Login details here
# bnhistory = breeze.get_historical_data(interval="1minute", from_date="2022-08-11T07:00:00.000Z",
#                                        to_date="2022-08-11T16:00:00.000Z", stock_code="CNXBAN", exchange_code="NFO",
#                                        product_type="options",expiry_date="2022-08-11T18:00:00.000Z",
#                                        right="call",strike_price=37200)
bnhistory = breeze.get_historical_data(interval="1minute",
                                       from_date="2022-8-12T07:00:00.000Z",
                                       to_date="2022-8-12T18:00:00.000Z",
                                       stock_code="TATSTE",
                                       exchange_code="NSE",
                                       product_type="others")
# # print(bnhistory)
sma = pd.DataFrame(bnhistory['Success'])
# print(sma.head())
sma['sma_20'] = sma['close'].rolling(10).mean()

trade_log = pd.DataFrame(columns='Stockcode,strike_price,call, Entry Time, Entry Price, Exit Time, Exit Price, take_profit'.split(','))
long_trade_triggered = 0
take_profit = 0.001
percentage = 0.001
for index, row in sma[1:].iterrows():
    previous_row = sma.iloc[index-1]
    # print(previous_row['sma_20'])
    # print("Prev SMA",previous_row['sma_20'],"Prev_row",previous_row['close'],"row:", row['close'],"SMA",row['sma_20'])
    # if (pd.to_numeric(previous_row['close']) < previous_row['sma_20']) & (pd.to_numeric(row['close']) > row['sma_20']) & (long_trade_triggered == 0):
    if (pd.to_numeric(previous_row['low']) < previous_row['sma_20']) & (pd.to_numeric(row['low']) > row['sma_20']) & (long_trade_triggered == 0):
        long_trade_triggered = 1
        take_profit = pd.to_numeric(row['close'])*(percentage/100 +1)
        # print("Buy", row['close'],row['datetime'],index)
        trade_log = trade_log.append({'Stockcode':row['stock_code'],'strike_price':row['strike_price'],'Call':'Buy', 'Entry Time':row['datetime'],'Entry Price' : row['close']},ignore_index=True)
    elif (long_trade_triggered == 1) &  (pd.to_numeric(previous_row['close']) > take_profit):
        # print("Exit", row['close'],row['datetime'],index)
        long_trade_triggered = 0
        trade_log = trade_log.append({'Exit Time' :row['datetime'],'Exit Price' : row['close']},ignore_index=True)
        take_profit = 0

trade_log['Exit Time'] = trade_log['Exit Time'].shift(-1)
trade_log['Exit Price'] = trade_log['Exit Price'].shift(-1)
trade_log['PnL'] = pd.to_numeric(trade_log['Exit Price'])- pd.to_numeric(trade_log['Entry Price'])
trade_log['take_profit'] = pd.to_numeric(trade_log['Exit Price'])*(percentage/100 + 1)
trade_log['Total Profit'] = pd.to_numeric(trade_log['PnL'])*100
trade_log.dropna(how='all', axis=1, inplace=True)
trade_log.dropna(inplace=True)
trade_log.reset_index(drop=True, inplace=True)
print(trade_log)
# trade_log.to_csv('C:\\Users\\mahen\\OneDrive\\Desktop\\backtest.csv')


