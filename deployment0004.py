from breeze_connect import BreezeConnect
from datetime import datetime, date, time, timedelta
import pandas as pd
import numpy as np
import datetime
import time
from alice_blue import *

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


def smatest():
Login details here

    # bnhistory = breeze.get_historical_data(interval="1minute", from_date="2022-08-25T07:00:00.000Z",
    #                                        to_date="2022-08-25T18:00:00.000Z", stock_code="CNXBAN",
    #                                        exchange_code="NFO", product_type="options",
    #                                        expiry_date="2022-09-01T18:00:00.000Z",
    #                                        right="call", strike_price=40500)
    bnhistory = breeze.get_historical_data(interval="1minute",from_date="2022-8-30T07:00:00.000Z",
                                           to_date="2022-8-30T18:00:00.000Z",stock_code="ITC",
                                           exchange_code="NSE",product_type="others")
    quote = breeze.get_quotes(stock_code="CNXBAN",
                              exchange_code="NFO",
                              expiry_date="2022-09-01T06:00:00.000Z",
                              product_type="options",
                              right="call",
                              strike_price=40500)
    #                            ,
    #                            expiry_date="2021-11-25T07:00:00.000Z",
    #                            right="others",
    #                            strike_price="0")

    bnh = pd.DataFrame(bnhistory['Success'])
    ohlc = pd.DataFrame(quote['Success'])
    # print(ohlc)
    # ohlc1 = ohlc.loc[ohlc['exchange_code'] == 'NSE']
    # print(ohlc["ltp"])
    ltp = ohlc["ltp"].iloc[0]
    # print(ltp)
    # print(round(ltp * 0.01))
    # print(round(ltp * 0.01, 1))
    # print(bnh)
    bnh['sma'] = bnh['close'].rolling(10).mean()
    bnh.drop(['open_interest'], axis=1)

    low = bnh['low'].iloc[-1]
    lowp = bnh['low'].iloc[-2]
    high = bnh['high'].iloc[-1]
    highp = bnh['high'].iloc[-2]
    # print(sma)
    sma = bnh['sma'].iloc[-1]
    smap = bnh['sma'].iloc[-2]
    # print(sma20,sma20p,low,lowp,high,highp)

    if ((sma < pd.to_numeric(low)) and (smap >= pd.to_numeric(lowp))):
        print(bnh.iloc[:, -8:].tail(2))
        print("SMA", sma, "<low", low, "SMAP", smap, ">lowp", lowp)
               # print(alice.place_order(transaction_type=TransactionType.Buy,
               #                         instrument=alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2022, 9, 1), is_fut=False, strike=40500, is_CE = True),
               #                         quantity=1,
               #                         order_type=OrderType.StopLossLimit,
               #                         product_type=ProductType.BracketOrder,
               #                         price=round(ltp, 1),
               #                         trigger_price=round(ltp * 0.1, 1),
               #                         stop_loss=round(ltp * 0.2, 1),
               #                         square_off=round(ltp * 0.1, 1),
               #                         trailing_sl=int(round(ltp * 0.01, 1)),
               #                         is_amo=False))
        print("Buy", bnh['close'].iloc[-1])
        print("Exit", round(ltp * 0.01, 1))
        print("######################################<  BUY  >###################################################")

        print(datetime.datetime.now())
    if ((sma > pd.to_numeric(high)) and (smap <= pd.to_numeric(highp))):
        print(bnh.iloc[:, -8:].tail(2))
        print("SMA", sma, ">high", high, "SMAP", smap, "<highp", highp)
               # print(alice.place_order(transaction_type=TransactionType.Buy,
               #                       instrument=alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2022, 9, 1), is_fut=False, strike=40500, is_CE = False),
               #                       quantity=1,
               #                       order_type=OrderType.StopLossLimit,
               #                       product_type=ProductType.BracketOrder,
               #                       price=round(ltp, 1),
               #                       trigger_price=round(ltp * 0.1, 1),
               #                       stop_loss=round(ltp * 0.1, 1),
               #                       square_off=round(ltp * 0.2, 1),
               #                       trailing_sl=int(round(ltp * 0.01, 1)),
               #                       is_amo=False))
        print("Sell", bnh['close'].iloc[-1])
        print("Exit", round(ltp * 0.01, 1))
        print("#######################################<  SELL  >##################################################")

        print(datetime.datetime.now())


now = datetime.datetime.now()

minute = now.minute

while minute <= 59:
    smatest()

    time.sleep(60)
    minute = now.minute
# Author  : Mahendran Paramasivan
