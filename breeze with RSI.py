from breeze_connect import BreezeConnect
from datetime import datetime,date,time,timedelta
import pandas as pd
import numpy as np
import time

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

breeze = BreezeConnect(api_key="yr5M5945t101!94ET&05H8225^1P1730")
breeze.generate_session(api_secret="n567E48667V4045OF27j7(&61026`04M", session_token="1587501")


bnce = breeze.get_historical_data(interval="1minute", from_date="2022-9-1T09:00:00.000Z",
                                       to_date="2022-9-2T18:00:00.000Z", stock_code="CNXBAN", exchange_code="NFO",
                                       product_type="options",expiry_date="2022-09-08T18:00:00.000Z",
                                       right="call",strike_price=39000)
# bnce = breeze.get_historical_data(interval="1minute",
#                                        from_date="2022-9-2T07:00:00.000Z",
#                                        to_date="2022-9-2T18:00:00.000Z",
#                                        stock_code="ITC",
#                                        exchange_code="NSE",
#                                        product_type="others")
# # print(bnhistory)
sma = pd.DataFrame(bnce['Success'])
# print(sma.head())

def rma(x, n, y0):
    a = (n-1) / n
    ak = a**np.arange(len(x)-1, -1, -1)
    return np.r_[np.full(n, np.nan), y0, np.cumsum(ak * x) / ak / n + y0 * a**np.arange(1, len(x)+1)]
sma['change'] = pd.to_numeric(sma['close']).diff()
sma['gain'] = sma.change.mask(sma.change < 0, 0.0)
sma['loss'] = -sma.change.mask(sma.change > 0, -0.0)
n = 14
sma['avg_gain'] = rma(sma.gain[n+1:].to_numpy(), n, np.nansum(sma.gain.to_numpy()[:n+1])/n)
sma['avg_loss'] = rma(sma.loss[n+1:].to_numpy(), n, np.nansum(sma.loss.to_numpy()[:n+1])/n)
sma['rs'] = sma.avg_gain / sma.avg_loss
sma['rsi_14'] = 100 - (100 / (1 + sma.rs))
# print(sma)
sma['sma'] = sma['close'].rolling(10).mean()
sma['low(-1)'] = sma['low'].shift(1)
sma['high(-1)'] = sma['high'].shift(1)
sma['rsi_14(-1)'] = sma['rsi_14'].shift(1)

conditions = [ (sma['rsi_14'] < 30) & (sma['rsi_14(-1)'] > 30),
               (sma['rsi_14'] > 70) & (sma['rsi_14(-1)'] < 70)
               ]
choices = ['Buy','Sell']
sma['signal'] = np.select(conditions,choices,default='')

conditions = [ (sma['rsi_14'] < 30) & (sma['rsi_14(-1)'] > 30),
               (sma['rsi_14'] > 70) & (sma['rsi_14(-1)'] < 70)
               ]
choices = [sma['close'],sma['close']]
sma['signal price'] = np.select(conditions,choices,default='')

# print(sma[["close","signal","signal price","datetime","rsi_14"]])

# print(sma)
# trade_log = pd.DataFrame(columns='Stockcode,strike_price,call, Entry Time, Entry Price, Exit Time, Exit Price, take_profit'.split(','))
trade_log = pd.DataFrame(columns='Stockcode,strike_price,call, Entry Time, Entry Price, Exit Time, Exit Price, take_profit'.split(','))
long_trade_triggered = 0
take_profit = 0
stop_lose = 0
tp_percentage = 5
sl_percentage = 0.001
for index, row in sma[1:].iterrows():
    previous_row = sma.iloc[index-1]
    if ((row['rsi_14'] < 30) and (previous_row['rsi_14'] > 30)):
        # print(row['rsi_14'], previous_row['rsi_14'], row['close'])
        long_trade_triggered = 1
        take_profit = pd.to_numeric(row['close'])*(1 + (tp_percentage/100))
        stop_lose = pd.to_numeric(row['close'])*(1 - (sl_percentage/100))
        # print("tp:",take_profit)
        # print("Close:",row['close'])
        # print("sl:",stop_lose)
        # print("Buy", row['close'],row['datetime'],index)
        trade_log = trade_log.append({'Stockcode':row['stock_code'],'strike_price':row['strike_price'],'Call':'Buy', 'Entry Time':row['datetime'],'Entry Price' : row['close']},ignore_index=True)
        # time.sleep(0.1)
    elif (long_trade_triggered == 1) & ((pd.to_numeric(row['close']) > take_profit) or (pd.to_numeric(row['close']) < stop_lose)):
        # print("Exit", row['close'],row['datetime'],index)
        long_trade_triggered = 0
        trade_log = trade_log.append({'Exit Time' :row['datetime'],'Exit Price' : row['close']},ignore_index=True)
        take_profit = 0
        stop_lose = 0
        # time.sleep(0.1)
    if ((row['rsi_14'] > 70) and (previous_row['rsi_14'] < 70)):
        long_trade_triggered = 2
        take_profit = pd.to_numeric(row['close']) * (1 - (tp_percentage / 100))
        stop_lose = pd.to_numeric(row['close']) * (1 + (sl_percentage / 100))
        # print("tp:",take_profit)
        # print("Close:",row['close'])
        # print("sl:",stop_lose)
        # print("Buy", row['close'],row['datetime'],index)
        trade_log = trade_log.append({'Stockcode': row['stock_code'], 'strike_price': row['strike_price'], 'Call': 'Sell','Entry Time': row['datetime'], 'Entry Price': row['close']}, ignore_index=True)
        # time.sleep(0.1)
    elif (long_trade_triggered == 2) & ((pd.to_numeric(row['close']) < take_profit) or (pd.to_numeric(row['close']) > stop_lose)):
        # print("Exit", row['close'],row['datetime'],index)
        long_trade_triggered = 0
        trade_log = trade_log.append({'Exit Time': row['datetime'], 'Exit Price': row['close']}, ignore_index=True)
        take_profit = 0
        stop_lose = 0
        # time.sleep(0.1)

trade_log['Exit Time'] = trade_log['Exit Time'].shift(-1)
trade_log['Exit Price'] = trade_log['Exit Price'].shift(-1)
# trade_log['PnL'] = pd.to_numeric(trade_log['Exit Price'])- pd.to_numeric(trade_log['Entry Price'])
trade_log['PnL'] = np.where(trade_log['Call']== 'Buy', (pd.to_numeric(trade_log['Exit Price'])- pd.to_numeric(trade_log['Entry Price'])), (pd.to_numeric(trade_log['Entry Price']) - pd.to_numeric(trade_log['Exit Price'])))
trade_log['take_profit'] = pd.to_numeric(trade_log['Entry Price'])*(tp_percentage/100 + 1)
trade_log['For a Lot'] = pd.to_numeric(trade_log['PnL'])*25
trade_log.dropna(how='all', axis=1, inplace=True)
trade_log.dropna(inplace=True)
trade_log.reset_index(drop=True, inplace=True)
trade_log['Total'] = trade_log['For a Lot'].cumsum()
print(trade_log)
trade_log.to_csv('C:\\Users\\mahen\\OneDrive\\Desktop\\takeprofit.csv')

# import xlwings as xw
# wb = xw.Book('C:\\Users\\mahen\\OneDrive\\Desktop\\takeprofit.csv')
# # wb.api.RefreshAll()
# sht1 = wb.sheets['Sheet1']
# xw.Range('A1').value = sma = trade_log
# xw.Range('A1').options(pd.DataFrame, expand='table').value