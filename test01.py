from breeze_connect import BreezeConnect
from datetime import datetime, date, time, timedelta
import pandas as pd
import numpy as np
import datetime
import time
from alice_blue import *

def smatest():
    breeze = BreezeConnect(api_key="83&2~83Y22K2018511yE&w60N2814B97")
    breeze.generate_session(api_secret="a68(7S85P4u$568491O#08374w0(6m6d", session_token="1547413")

    access_token = AliceBlue.login_and_get_access_token(username='AB133347', password='pragati@3', twoFA='1985',
                                                        api_secret='bb4azbDnhxfJ7bbTKfd4gWjN8yc3IOXLykCLOfqvrdU3ixAONzyqe6dT0qh4xaeZ',
                                                        app_id='jvbqTE5sF8')
    alice = AliceBlue(username='AB133347', password='pragati@3', access_token=access_token)

    bnhistory = breeze.get_historical_data(interval="1minute", from_date="2022-08-25T07:00:00.000Z",
                                           to_date="2022-08-25T18:00:00.000Z", stock_code="CNXBAN",
                                           exchange_code="NFO", product_type="options",
                                           expiry_date="2022-09-01T18:00:00.000Z",
                                           right="call",strike_price=40500)
    # bnhistory = breeze.get_historical_data(interval="1minute",from_date="2022-8-18T07:00:00.000Z",
    #                                        to_date="2022-8-18T18:00:00.000Z",stock_code="ITC",
    #                                        exchange_code="NSE",product_type="others")
    print(bnhistory)
    # quote = breeze.get_quotes(stock_code="CNXBAN",
    #             exchange_code="NFO",
    #             expiry_date="2022-09-01T06:00:00.000Z",
    #             product_type="options",
    #             right="call",
    #             strike_price=40500)
    # print(quote)
    #                            ,
    #                            expiry_date="2021-11-25T07:00:00.000Z",
    #                            right="others",
    #                            strike_price="0")

    # sma = pd.DataFrame(bnhistory['Success'])
    # print(sma)
    # ohlc = pd.DataFrame(quote['Success'])
    # print(ohlc)
    # ohlc1 = ohlc.loc[ohlc['exchange_code'] == 'NSE']
    # print(ohlc["ltp"])
    # ltp = ohlc["ltp"].iloc[0]
    # # print(ltp)
    # # print(round(ltp * 0.01))
    # # print(round(ltp * 0.01, 1))
    # # print(sma)
    # sma['sma_20'] = sma['close'].rolling(10).mean()
    # low = sma['low'].iloc[-1]
    # lowp = sma['low'].iloc[-2]
    # high = sma['high'].iloc[-1]
    # highp = sma['high'].iloc[-2]
    # # print(sma)
    # sma20 = sma['sma_20'].iloc[-1]
    # sma20p = sma['sma_20'].iloc[-2]
    # # print(sma20,sma20p,low,lowp,high,highp)
    #
    #
    # if sma20 < pd.to_numeric(low) and sma20p > pd.to_numeric(lowp):
    #     print(alice.place_order(transaction_type=TransactionType.Buy,
    #                             instrument=alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2022, 9, 1), is_fut=False, strike=40500, is_CE = True),
    #                             quantity=1,
    #                             order_type=OrderType.StopLossLimit,
    #                             product_type=ProductType.BracketOrder,
    #                             price=round(ltp, 1),
    #                             trigger_price=round(ltp * 0.01, 1),
    #                             stop_loss=round(ltp * 0.01, 1),
    #                             square_off=round(ltp * 0.01, 1),
    #                             trailing_sl=int(round(ltp * 0.01, 1)),
    #                             is_amo=False))
    #     print(round(ltp * 0.01))
    #     print("Buy",sma['close'].iloc[-1])
    # if sma20 > pd.to_numeric(high) and sma20p < pd.to_numeric(highp):
    #     print(
    #         alice.place_order(transaction_type=TransactionType.Buy,
    #                           instrument=alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2022, 9, 1), is_fut=False, strike=40500, is_CE = False),
    #                           quantity=1,
    #                           order_type=OrderType.StopLossLimit,
    #                           product_type=ProductType.BracketOrder,
    #                           price=round(ltp, 1),
    #                           trigger_price=round(ltp * 0.01, 1),
    #                           stop_loss=round(ltp * 0.01, 1),
    #                           square_off=round(ltp * 0.01, 1),
    #                           trailing_sl=int(round(ltp * 0.01, 1)),
    #                           is_amo=False))
    #     print(round(ltp * 0.01))
    #     print("Sell",sma['close'].iloc[-1])
smatest()
# now = datetime.datetime.now()
#
# minute = now.minute
#
# while minute <= 59:
#     smatest()
#     print(datetime.datetime.now())
#     time.sleep(60)
#     minute = now.minute
# # Author  : Mahendran Paramasivan
