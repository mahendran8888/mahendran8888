from datetime import datetime
from datetime import datetime, date, time, timedelta
from breeze_connect import BreezeConnect
import pandas as pd
import numpy as np
import datetime
import time
from alice_blue import *
from nsepython import *



def smatest():
    from datetime import datetime
    breeze = BreezeConnect(api_key="6c61)R6801q66g3183I44C8934$513R0")
    breeze.generate_session(api_secret="54=K032701*6N9Iw6P97M335F+X86w68", session_token="1553069")

    access_token = AliceBlue.login_and_get_access_token(username='AB133347', password='pragati@3', twoFA='1985',
                                                        api_secret='bb4azbDnhxfJ7bbTKfd4gWjN8yc3IOXLykCLOfqvrdU3ixAONzyqe6dT0qh4xaeZ',
                                                        app_id='jvbqTE5sF8')
    alice = AliceBlue(username='AB133347', password='pragati@3', access_token=access_token)
    symbol = 'BANKNIFTY'
    stock_code = "CNXBAN"
    currentExpiry = nse_expirydetails(nse_optionchain_scrapper(symbol), 0)[0]
    strike = 40500




    bnhistory = breeze.get_historical_data(interval="1minute", from_date=datetime.now().strftime('%Y-%m-%dT09:00:00.000Z'),
                                           to_date=datetime.now().strftime('%Y-%m-%dT16:00:00.000Z'), stock_code=stock_code,
                                           exchange_code="NFO", product_type="options",
                                           expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                                           right="call",strike_price=strike)
    # bnhistory = breeze.get_historical_data(interval="1minute",from_date="2022-8-18T07:00:00.000Z",
    #                                        to_date="2022-8-18T18:00:00.000Z",stock_code="ITC",
    #                                        exchange_code="NSE",product_type="others")
    quote = breeze.get_quotes(stock_code=stock_code,
                exchange_code="NFO",
                expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                product_type="options",
                right="call",
                strike_price=strike)
    #                            ,
    #                            expiry_date="2021-11-25T07:00:00.000Z",
    #                            right="others",
    #                            strike_price="0")

    sma = pd.DataFrame(bnhistory['Success'])
    ohlc = pd.DataFrame(quote['Success'])
    # print(ohlc)
    # ohlc1 = ohlc.loc[ohlc['exchange_code'] == 'NSE']
    # print(ohlc["ltp"])
    ltp = ohlc["ltp"].iloc[0]
    # print(ltp)
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


    if sma20 < pd.to_numeric(low) and sma20p > pd.to_numeric(lowp):
        print(alice.place_order(transaction_type=TransactionType.Buy,
                                instrument=alice.get_instrument_for_fno(symbol = symbol, expiry_date=currentExpiry, is_fut=False, strike=strike, is_CE = True),
                                quantity=1,
                                order_type=OrderType.StopLossLimit,
                                product_type=ProductType.BracketOrder,
                                price=round(ltp, 1),
                                trigger_price=round(ltp * 0.01, 1),
                                stop_loss=round(ltp * 0.01, 1),
                                square_off=round(ltp * 0.01, 1),
                                trailing_sl=int(round(ltp * 0.01, 1)),
                                is_amo=False))
        print(round(ltp * 0.01))
        print("Buy",sma['close'].iloc[-1])
        print(datetime.datetime.now())
    if sma20 > pd.to_numeric(high) and sma20p < pd.to_numeric(highp):
        print(
            alice.place_order(transaction_type=TransactionType.Buy,
                              instrument=alice.get_instrument_for_fno(symbol = symbol, expiry_date=currentExpiry, is_fut=False, strike=strike, is_CE = False),
                              quantity=1,
                              order_type=OrderType.StopLossLimit,
                              product_type=ProductType.BracketOrder,
                              price=round(ltp, 1),
                              trigger_price=round(ltp * 0.01, 1),
                              stop_loss=round(ltp * 0.01, 1),
                              square_off=round(ltp * 0.01, 1),
                              trailing_sl=int(round(ltp * 0.01, 1)),
                              is_amo=False))
        print(round(ltp * 0.01))
        print("Sell",sma['close'].iloc[-1])
        print(datetime.datetime.now())
# smatest()
from datetime import datetime, date, time, timedelta
import datetime
import time

now = datetime.datetime.now()
minute = now.minute

while minute <= 59:
    smatest()
    # print(datetime.datetime.now())
    time.sleep(60)
    minute = now.minute
# # Author  : Mahendran Paramasivan