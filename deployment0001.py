
# pip install breeze-connect

# pip install alice-blue

from breeze_connect import BreezeConnect
from datetime import datetime, date, time, timedelta
import pandas as pd
import numpy as np
import datetime
import time
from alice_blue import *

def smatest():
    breeze = BreezeConnect(api_key="2y25Xg84021k517@2i156U4~V95*A683")
    breeze.generate_session(api_secret="5N24lU133416Z63H3o5s89R6442v4X8b", session_token="1520265")

    access_token = AliceBlue.login_and_get_access_token(username='AB133347', password='pragati@3', twoFA='1985',
                                                        api_secret='bb4azbDnhxfJ7bbTKfd4gWjN8yc3IOXLykCLOfqvrdU3ixAONzyqe6dT0qh4xaeZ',
                                                        app_id='jvbqTE5sF8')
    alice = AliceBlue(username='AB133347', password='pragati@3', access_token=access_token)

    # bnhistory = breeze.get_historical_data(interval="1minute", from_date="2022-08-08T07:00:00.000Z",
    #                                        to_date="2022-08-08T18:00:00.000Z", stock_code="CNXBAN",
    #                                        exchange_code="NFO", product_type="options",
    #                                        expiry_date="2022-08-11T18:00:00.000Z",
    #                                        right="call",strike_price=38600)
    bnhistory = breeze.get_historical_data(interval="1minute",from_date="2022-8-18T07:00:00.000Z",
                                           to_date="2022-8-18T18:00:00.000Z",stock_code="ITC",
                                           exchange_code="NSE",product_type="others")
    quote = breeze.get_quotes(stock_code="ITC",
                exchange_code="NSE",
                expiry_date="2022-08-04T06:00:00.000Z",
                product_type="cash",
                right="others",
                strike_price="0")
    #                            ,
    #                            expiry_date="2021-11-25T07:00:00.000Z",
    #                            right="others",
    #                            strike_price="0")

    sma = pd.DataFrame(bnhistory['Success'])
    ohlc = pd.DataFrame(quote['Success'])

    ohlc1 = ohlc.loc[ohlc['exchange_code'] == 'NSE']
    # print(ohlc1["ltp"])
    ltp = ohlc1["ltp"].iloc[0]
    # print(type(ltp))
    # print(round(ltp * 0.01))
    # print(round(ltp * 0.01, 1))
    # print(sma)
    sma['sma_20'] = sma['close'].rolling(10).mean()
    low = sma['low'].iloc[-1]
    lowp = sma['low'].iloc[-2]
    high = sma['high'].iloc[-1]
    highp = sma['high'].iloc[-2]
    # print(sma)
    sma20 = sma['sma_20'].iloc[-1]
    sma20p = sma['sma_20'].iloc[-2]
    # print(sma20,sma20p,low,lowp,high,highp)
    # print(alice.place_order(transaction_type=TransactionType.Sell,
    #                         instrument=alice.get_instrument_by_symbol('NSE', 'ITC'),
    #                         quantity=1,
    #                         order_type=OrderType.StopLossLimit,
    #                         product_type=ProductType.BracketOrder,
    #                         price=round(ltp, 1),
    #                         trigger_price=round(ltp * 0.01, 1),
    #                         stop_loss=round(ltp * 0.01, 1),
    #                         square_off=round(ltp * 0.01, 1),
    #                         trailing_sl=1,
    #                         is_amo=False))

    if sma20 < pd.to_numeric(low) and sma20p > pd.to_numeric(lowp):
        print(alice.place_order(transaction_type=TransactionType.Sell,
                                instrument=alice.get_instrument_by_symbol('NSE', 'ITC'),
                                quantity=1,
                                order_type=OrderType.StopLossLimit,
                                product_type=ProductType.BracketOrder,
                                price=round(ltp, 1),
                                trigger_price=round(ltp * 0.01, 1),
                                stop_loss=round(ltp * 0.01, 1),
                                square_off=round(ltp * 0.01, 1),
                                trailing_sl=round(ltp * 0.01, 1),
                                is_amo=False))
        print(round(ltp * 0.01))
        print("Buy",sma['close'].iloc[-1])
    if sma20 > pd.to_numeric(high) and sma20p < pd.to_numeric(highp):
        print(
            alice.place_order(transaction_type=TransactionType.Sell,
                              instrument=alice.get_instrument_by_symbol('NSE', 'ITC'),
                              quantity=1,
                              order_type=OrderType.StopLossLimit,
                              product_type=ProductType.BracketOrder,
                              price=round(ltp, 1),
                              trigger_price=round(ltp * 0.01, 1),
                              stop_loss=round(ltp * 0.01, 1),
                              square_off=round(ltp * 0.01, 1),
                              trailing_sl=round(ltp * 0.01, 1),
                              is_amo=False))
        print(round(ltp * 0.01))
        print("Sell",sma['close'].iloc[-1])
now = datetime.datetime.now()

minute = now.minute

while minute <= 59:
    smatest()
    print(datetime.datetime.now())
    time.sleep(60)
    minute = now.minute
# Author  : Mahendran Paramasivan