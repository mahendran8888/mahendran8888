from breeze_connect import BreezeConnect
from datetime import datetime,date,time,timedelta
import pandas as pd
import numpy as np
from credentials001 import *
import requests
import datetime
import time
from nsepython import *
import json
from datetime import datetime
import itertools
from dateutil.relativedelta import relativedelta, TH
import datetime
import warnings
# from openpyxl.workbook import Workbook
# from openpyxl import Workbook

warnings.simplefilter(action='ignore',category=FutureWarning)
t1=time.time()
requests.packages.urllib3.util.connection.HAS_IPV6 = False
currentExpiry = nse_expirydetails(nse_optionchain_scrapper('BANKNIFTY'), 0)[0]
# print(currentExpiry-timedelta(days=7),currentExpiry)


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

breeze = BreezeConnect(api_key=api_key)
breeze.generate_session(api_secret=api_secret, session_token=session_token)

df = breeze.get_historical_data(interval="1day",
                            from_date= "2024-1-1T07:00:00.000Z",
                            to_date= "2024-1-31T07:00:00.000Z",
                            stock_code="CNXBAN",
                            exchange_code="NSE",
                            product_type="cash")

# print(pd.DataFrame(df['Success']))
open = pd.DataFrame(df['Success'])['open'].astype(float)
date = pd.DataFrame(df['Success'])['datetime']
date1 = pd.to_datetime(date).dt.date
open_round = round(open,-2)
# print(date,date1,open_round)
strangle_price = 0
df_bnce1 = []
df_bnpe1 = []
for open_round,date,date1 in zip(open_round,date,date1):

    holidays = pd.DataFrame(nse_holidays("trading")['CBM'])
    hd = holidays['tradingDate'].to_list()

    day = date1
    n = 2 # 2 for wednesday
    wk_wed_date = day + timedelta(7 - ((day.weekday() - n + 7) if day.weekday() - n < 0 else day.weekday() - n))
    th = wk_wed_date + relativedelta(day=31, weekday=TH(-1))
    mon_th_date = th if ((th - wk_wed_date).days) ==1 else wk_wed_date
    expirydate = ((mon_th_date - timedelta(days=1)) if mon_th_date.strftime("%d-%b-%Y") in hd else mon_th_date)

    bnce = breeze.get_historical_data(interval="1minute", from_date=date1.strftime('%Y-%m-%dT06:00:00.000Z'),to_date=date1.strftime('%Y-%m-%dT06:00:00.000Z'), stock_code="CNXBAN",
                                      exchange_code="NFO",product_type="options",expiry_date=expirydate.strftime('%Y-%m-%dT06:00:00.000Z'),
                                      right="call", strike_price=open_round+strangle_price)
    bnpe = breeze.get_historical_data(interval="1minute", from_date=date1.strftime('%Y-%m-%dT06:00:00.000Z'),to_date=date1.strftime('%Y-%m-%dT06:00:00.000Z'), stock_code="CNXBAN",
                                      exchange_code="NFO",product_type="options",expiry_date=expirydate.strftime('%Y-%m-%dT06:00:00.000Z'),
                                      right="put", strike_price=open_round-strangle_price)
    # print(bnce)
    df_bnce = pd.DataFrame(bnce['Success'])
    df_bnpe = pd.DataFrame(bnpe['Success'])
    # print(df_bnce)
    df_bnce1.append(df_bnce)
    df_bnpe1.append(df_bnpe)
df_bnce1 = pd.concat(df_bnce1)
df_bnpe1 = pd.concat(df_bnpe1)
# df_bn_ce_pe =
# print(df_bnce1,df_bnpe1)
# bn_ce_pe = df_bnce1.append(df_bnpe1)
# print(bn_ce_pe)

trade_log = pd.DataFrame(columns='Stockcode,right,strike_price,call, Entry Time, Entry Price, Exit Time, Exit Price, take_profit'.split(','))
ce_long_trade_triggered = 0
pe_long_trade_triggered = 0
take_profit = 0
stop_lose = 0
tp_percentage = 10
sl_percentage = 100


for index, row in df_bnce1[1:].iterrows():
    if index == 1:
        # print(row)
        trade_log = trade_log.append(
            {'Stockcode': row['stock_code'],'right': row['right'], 'strike_price': row['strike_price'], 'Call': 'Buy',
             'Entry Time': row['datetime'], 'Entry Price': row['close']}, ignore_index=True)
        ce_long_trade_triggered = 1
    elif ce_long_trade_triggered == 1 and index == 360:
        trade_log = trade_log.append({'Exit Time': row['datetime'], 'Exit Price': row['close']}, ignore_index=True)
        ce_long_trade_triggered = 0

for index, row in df_bnpe1[1:].iterrows():
    if index == 1 and pe_long_trade_triggered == 0:
        trade_log = trade_log.append(
            {'Stockcode': row['stock_code'],'right': row['right'], 'strike_price': row['strike_price'], 'Call': 'Buy',
             'Entry Time': row['datetime'], 'Entry Price': row['close']}, ignore_index=True)
        pe_long_trade_triggered = 1
    elif pe_long_trade_triggered == 1 and index == 360:
        trade_log = trade_log.append({'Exit Time': row['datetime'], 'Exit Price': row['close']}, ignore_index=True)
        pe_long_trade_triggered = 0


trade_log['Exit Time'] = trade_log['Exit Time'].shift(-1)
trade_log['Exit Price'] = trade_log['Exit Price'].shift(-1)
trade_log['PnL'] = np.where(trade_log['Call']== 'Buy', (pd.to_numeric(trade_log['Exit Price'])- pd.to_numeric(trade_log['Entry Price'])), (pd.to_numeric(trade_log['Entry Price']) - pd.to_numeric(trade_log['Exit Price'])))
trade_log.dropna(how='all', axis=1, inplace=True)
trade_log.dropna(inplace=True)
trade_log.reset_index(drop=True, inplace=True)
trade_log['For a Lot'] = pd.to_numeric(trade_log['PnL'])*15
trade_log['Total'] = trade_log['For a Lot'].cumsum()
# trade_log['date'] = pd.to_datetime(trade_log['Entry Time']).dt.date
trade_log.sort_values(by='Entry Time')
print(trade_log)
