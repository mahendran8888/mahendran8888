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
# from openpyxl.workbook import Workbook
# from openpyxl import Workbook

import warnings
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

def rsi_buy(d1,d2,tp,sl):
    x=d1.strftime('%Y-%m-%dT06:00:00.000Z')
    y=d2.strftime('%Y-%m-%dT06:00:00.000Z')
    df = breeze.get_historical_data(interval="1day",
                                from_date= x,
                                to_date= y,
                                stock_code="CNXBAN",
                                exchange_code="NSE",
                                product_type="cash")

    # print(pd.DataFrame(df['Success']))
    open = pd.DataFrame(df['Success'])['open'].astype(float)
    date = pd.DataFrame(df['Success'])['datetime']
    date1 = pd.to_datetime(date).dt.date
    open_round = round(open, -2)
    # print(date,date1,open_round)
    strangle_price = 0
    df_bnce1 = []
    df_bnpe1 = []
    for open_round, date, date1 in zip(open_round, date, date1):
        holidays = pd.DataFrame(nse_holidays("trading")['CBM'])
        hd = holidays['tradingDate'].to_list()

        day = date1
        n = 2  # 2 for wednesday
        wk_wed_date = day + timedelta(7 - ((day.weekday() - n + 7) if day.weekday() - n < 0 else day.weekday() - n))
        th = wk_wed_date + relativedelta(day=31, weekday=TH(-1))
        mon_th_date = th if ((th - wk_wed_date).days) == 1 else wk_wed_date
        expirydate = ((mon_th_date - timedelta(days=1)) if mon_th_date.strftime("%d-%b-%Y") in hd else mon_th_date)

        bnce = breeze.get_historical_data(interval="1minute", from_date=date1.strftime('%Y-%m-%dT06:00:00.000Z'),
                                          to_date=date1.strftime('%Y-%m-%dT06:00:00.000Z'), stock_code="CNXBAN",
                                          exchange_code="NFO", product_type="options",
                                          expiry_date=expirydate.strftime('%Y-%m-%dT06:00:00.000Z'),
                                          right="call", strike_price=open_round + strangle_price)
        bnpe = breeze.get_historical_data(interval="1minute", from_date=date1.strftime('%Y-%m-%dT06:00:00.000Z'),
                                          to_date=date1.strftime('%Y-%m-%dT06:00:00.000Z'), stock_code="CNXBAN",
                                          exchange_code="NFO", product_type="options",
                                          expiry_date=expirydate.strftime('%Y-%m-%dT06:00:00.000Z'),
                                          right="put", strike_price=open_round - strangle_price)
        # print(bnce)
        df_bnce = pd.DataFrame(bnce['Success'])
        df_bnpe = pd.DataFrame(bnpe['Success'])
        # print(df_bnce)
        df_bnce1.append(df_bnce)
        df_bnpe1.append(df_bnpe)
    dfbnce1 = pd.concat(df_bnce1)
    dfbnpe1 = pd.concat(df_bnpe1)

    def rma(x, n, y0):
        a = (n - 1) / n
        ak = a ** np.arange(len(x) - 1, -1, -1)
        return np.r_[np.full(n, np.nan), y0, np.cumsum(ak * x) / ak / n + y0 * a ** np.arange(1, len(x) + 1)]

    dfbnce1['change'] = pd.to_numeric(dfbnce1['close']).diff()
    dfbnce1['gain'] = dfbnce1.change.mask(dfbnce1.change < 0, 0.0)
    dfbnce1['loss'] = -dfbnce1.change.mask(dfbnce1.change > 0, -0.0)
    n = 14
    dfbnce1['avg_gain'] = rma(dfbnce1.gain[n + 1:].to_numpy(), n, np.nansum(dfbnce1.gain.to_numpy()[:n + 1]) / n)
    dfbnce1['avg_loss'] = rma(dfbnce1.loss[n + 1:].to_numpy(), n, np.nansum(dfbnce1.loss.to_numpy()[:n + 1]) / n)
    dfbnce1['rs'] = dfbnce1.avg_gain / dfbnce1.avg_loss
    dfbnce1['rsi_14'] = 100 - (100 / (1 + dfbnce1.rs))

    #################### RSI CE #################
    # print(dfbnce1)
    dfbnce1['dfbnce1'] = dfbnce1['close'].rolling(10).mean()
    dfbnce1['low(-1)'] = dfbnce1['low'].shift(1)
    dfbnce1['high(-1)'] = dfbnce1['high'].shift(1)
    dfbnce1['rsi_14(-1)'] = dfbnce1['rsi_14'].shift(1)

    conditions = [(dfbnce1['rsi_14'] < 30) & (dfbnce1['rsi_14(-1)'] > 30),
                  (dfbnce1['rsi_14'] > 70) & (dfbnce1['rsi_14(-1)'] < 70)
                  ]
    choices = ['Buy', 'Sell']
    dfbnce1['signal'] = np.select(conditions, choices, default='')

    conditions = [(dfbnce1['rsi_14'] < 30) & (dfbnce1['rsi_14(-1)'] > 30),
                  (dfbnce1['rsi_14'] > 70) & (dfbnce1['rsi_14(-1)'] < 70)
                  ]
    choices = [dfbnce1['close'], dfbnce1['close']]
    dfbnce1['signal price'] = np.select(conditions, choices, default='')

    # print(dfbnce1[["close", "signal", "signal price", "datetime", "rsi_14"]])

    dfbnpe1['change'] = pd.to_numeric(dfbnpe1['close']).diff()
    dfbnpe1['gain'] = dfbnpe1.change.mask(dfbnpe1.change < 0, 0.0)
    dfbnpe1['loss'] = -dfbnpe1.change.mask(dfbnpe1.change > 0, -0.0)
    n = 14
    dfbnpe1['avg_gain'] = rma(dfbnpe1.gain[n + 1:].to_numpy(), n, np.nansum(dfbnpe1.gain.to_numpy()[:n + 1]) / n)
    dfbnpe1['avg_loss'] = rma(dfbnpe1.loss[n + 1:].to_numpy(), n, np.nansum(dfbnpe1.loss.to_numpy()[:n + 1]) / n)
    dfbnpe1['rs'] = dfbnpe1.avg_gain / dfbnpe1.avg_loss
    dfbnpe1['rsi_14'] = 100 - (100 / (1 + dfbnpe1.rs))

    #################### RSI PE #################
    # print(dfbnpe1)
    dfbnpe1['dfbnpe1'] = dfbnpe1['close'].rolling(10).mean()
    dfbnpe1['low(-1)'] = dfbnpe1['low'].shift(1)
    dfbnpe1['high(-1)'] = dfbnpe1['high'].shift(1)
    dfbnpe1['rsi_14(-1)'] = dfbnpe1['rsi_14'].shift(1)

    conditions = [(dfbnpe1['rsi_14'] < 30) & (dfbnpe1['rsi_14(-1)'] > 30),
                  (dfbnpe1['rsi_14'] > 70) & (dfbnpe1['rsi_14(-1)'] < 70)
                  ]
    choices = ['Buy', 'Sell']
    dfbnpe1['signal'] = np.select(conditions, choices, default='')

    conditions = [(dfbnpe1['rsi_14'] < 30) & (dfbnpe1['rsi_14(-1)'] > 30),
                  (dfbnpe1['rsi_14'] > 70) & (dfbnpe1['rsi_14(-1)'] < 70)
                  ]
    choices = [dfbnpe1['close'], dfbnpe1['close']]
    dfbnpe1['signal price'] = np.select(conditions, choices, default='')

    # print(dfbnpe1[["close", "signal", "signal price", "datetime", "rsi_14"]])

    # print(dfbnce)
    # trade_log = pd.DataFrame(columns='Stockcode,strike_price,call, Entry Time, Entry Price, Exit Time, Exit Price, take_profit'.split(','))
    trade_log = pd.DataFrame(
        columns='Stockcode,Right,strike_price,call, Entry Time, Entry Price, Exit Time, Exit Price, take_profit'.split(
            ','))
    long_trade_triggered = 0
    take_profit = 0
    stop_lose = 0
    tp_percentage = tp
    sl_percentage = sl
    for index, row in dfbnce1[1:].iterrows():
        previous_row = dfbnce1.iloc[index - 1]
        if   (long_trade_triggered == 0) & ((row['rsi_14'] < 30) and (previous_row['rsi_14'] > 30) and index < 314):
            # print(row['rsi_14'], previous_row['rsi_14'], row['close'])
            long_trade_triggered = 1
            take_profit = pd.to_numeric(row['close']) * (1 + (tp_percentage / 100))
            stop_lose = pd.to_numeric(row['close']) * (1 - (sl_percentage / 100))
            # print("tp:",take_profit)
            # print("Close:",row['close'])
            # print("sl:",stop_lose)
            # print("Buy", row['close'],row['datetime'],index)
            trade_log = trade_log.append(
                {'Stockcode': row['stock_code'], 'Right': row['right'], 'strike_price': row['strike_price'],
                 'Call': 'Buy', 'Entry Time': row['datetime'], 'Entry Price': row['close']}, ignore_index=True)
            # time.sleep(0.1)
        elif (long_trade_triggered == 1) & ((pd.to_numeric(row['close']) > take_profit) or (
                pd.to_numeric(row['close']) < stop_lose) or index == 359):
            # print("Exit", row['close'],row['datetime'],index)
            long_trade_triggered = 0
            trade_log = trade_log.append({'Exit Time': row['datetime'], 'Exit Price': row['close']}, ignore_index=True)
            take_profit = 0
            stop_lose = 0
            time.sleep(0.1)

    for index, row in dfbnpe1[1:].iterrows():
        previous_row = dfbnpe1.iloc[index - 1]
        if   (long_trade_triggered == 0) & ((row['rsi_14'] < 30) and (previous_row['rsi_14'] > 30) and index < 314):
            # print(row['rsi_14'], previous_row['rsi_14'], row['close'])
            long_trade_triggered = 1
            take_profit = pd.to_numeric(row['close']) * (1 + (tp_percentage / 100))
            stop_lose = pd.to_numeric(row['close']) * (1 - (sl_percentage / 100))
            # print("tp:",take_profit)
            # print("Close:",row['close'])
            # print("sl:",stop_lose)
            # print("Buy", row['close'],row['datetime'],index)
            trade_log = trade_log.append(
                {'Stockcode': row['stock_code'], 'Right': row['right'], 'strike_price': row['strike_price'],
                 'Call': 'Buy', 'Entry Time': row['datetime'], 'Entry Price': row['close']}, ignore_index=True)
            # time.sleep(0.1)
        elif (long_trade_triggered == 1) & ((pd.to_numeric(row['close']) > take_profit) or (
                pd.to_numeric(row['close']) < stop_lose) or index == 359):
            # print("Exit", row['close'],row['datetime'],index)
            long_trade_triggered = 0
            trade_log = trade_log.append({'Exit Time': row['datetime'], 'Exit Price': row['close']}, ignore_index=True)
            take_profit = 0
            stop_lose = 0
            time.sleep(0.1)

    trade_log['Exit Time'] = trade_log['Exit Time'].shift(-1)
    trade_log['Exit Price'] = trade_log['Exit Price'].shift(-1)
    # trade_log['PnL'] = pd.to_numeric(trade_log['Exit Price'])- pd.to_numeric(trade_log['Entry Price'])
    trade_log['PnL'] = np.where(trade_log['Call'] == 'Buy',
                                (pd.to_numeric(trade_log['Exit Price']) - pd.to_numeric(trade_log['Entry Price'])),
                                (pd.to_numeric(trade_log['Entry Price']) - pd.to_numeric(trade_log['Exit Price'])))
    trade_log['take_profit'] = pd.to_numeric(trade_log['Entry Price']) * (tp_percentage / 100 + 1)
    trade_log['For a Lot'] = pd.to_numeric(trade_log['PnL']) * 15
    trade_log.dropna(how='all', axis=1, inplace=True)
    trade_log.dropna(inplace=True)
    trade_log.reset_index(drop=True, inplace=True)
    trade_log['Total'] = trade_log['For a Lot'].cumsum()
    # warnings.simplefilter(action='ignore',category=FutureWarning)
    print(trade_log)

# rsi_buy(datetime.datetime(2024,1,25),datetime.datetime(2024,1,25),0.1,100)