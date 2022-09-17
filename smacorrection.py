from alice_blue import *
def smatest():
    from breeze_connect import BreezeConnect
    from datetime import datetime,date,time,timedelta
    import pandas as pd
    import numpy as np
    import math
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    breeze = BreezeConnect(api_key="1kA440t7401177L329z1I79H5R0J49y1")
    breeze.generate_session(api_secret="~2211636ES2RD9462951909401o+e597", session_token="1536299")

    access_token = AliceBlue.login_and_get_access_token(username='AB133347', password='pragati@3', twoFA='1985',
                                                        api_secret='bb4azbDnhxfJ7bbTKfd4gWjN8yc3IOXLykCLOfqvrdU3ixAONzyqe6dT0qh4xaeZ',
                                                        app_id='jvbqTE5sF8')
    alice = AliceBlue(username='AB133347', password='pragati@3', access_token=access_token)

    stock_code = "ONGC"
    ohlc = breeze.get_historical_data(interval="1minute",from_date=datetime.now().strftime('%Y-%m-%dT09:00:00.000Z'),
                                           to_date=datetime.now().strftime('%Y-%m-%dT16:00:00.000Z'),stock_code=stock_code,
                                           exchange_code="NSE",product_type="others")
    # Get quotes of mentioned stock-code
    quote = breeze.get_quotes(stock_code=stock_code,
                      exchange_code="NSE",
                      expiry_date="",
                      product_type="cash",
                      right="others",
                      strike_price="0")
    # print(quote)
    qf = pd.DataFrame(quote['Success'])
    # print(qf)
    ltp = qf.loc[qf['exchange_code']=='NSE', 'ltp'].loc[0]
    print(ltp, round(ltp*0.99, -1), round(ltp*0.01, 1), round(ltp*0.0025, 1), round(ltp*0.01))
    # print(round(ltp*0.0025, 1))
    sma = pd.DataFrame(ohlc['Success'])
    # print(sma)
    sma['sma_20'] = sma['close'].rolling(10).mean()
    # print(sma)
    # ltp = sma['close'].iloc[-1]
    # print(ltp)
    low = sma['low'].iloc[-1]
    # print(low)
    lowp = sma['low'].iloc[-2]
    high = sma['high'].iloc[-1]
    highp = sma['high'].iloc[-2]
    # print(sma)
    sma20 = sma['sma_20'].iloc[-1]
    sma20p = sma['sma_20'].iloc[-2]
    # print(sma20,sma20p,low,lowp,high,highp)
    # print(alice.place_order(transaction_type=TransactionType.Buy,
    #                         instrument=alice.get_instrument_by_symbol('NSE', stock_code),
    #                         quantity=1,
    #                         order_type=OrderType.StopLossLimit,
    #                         product_type=ProductType.BracketOrder,
    #                         price=ltp,
    #                         trigger_price=round(ltp*0.99, -1),
    #                         stop_loss=float(round(ltp*0.003)),
    #                         square_off=float(round(ltp*0.005)),
    #                         trailing_sl=round(ltp*0.003),
    #                         is_amo=False))

    if sma20 < pd.to_numeric(low) and sma20p > pd.to_numeric(lowp):
        print("Buy", sma['close'].iloc[-1])
        print(alice.place_order(transaction_type=TransactionType.Buy,
                                instrument=alice.get_instrument_by_symbol('NSE', stock_code),
                                quantity=1,
                                order_type=OrderType.StopLossLimit,
                                product_type=ProductType.BracketOrder,
                                price=ltp,
                                trigger_price=round(ltp * 0.99, -1),
                                stop_loss=float(round(ltp * 0.01, 1)),
                                square_off=float(round(ltp*0.0025, 1)),
                                trailing_sl=round(ltp * 0.01),
                                is_amo=False))

    if sma20 > pd.to_numeric(high) and sma20p < pd.to_numeric(highp):
        print(alice.place_order(transaction_type=TransactionType.Sell,
                                instrument=alice.get_instrument_by_symbol('NSE', stock_code),
                                quantity=1,
                                order_type=OrderType.StopLossLimit,
                                product_type=ProductType.BracketOrder,
                                price=ltp,
                                trigger_price=round(ltp * 0.99, -1),
                                stop_loss=float(round(ltp * 0.01, 1)),
                                square_off=float(round(ltp*0.0025, 1)),
                                trailing_sl=round(ltp * 0.01),
                                is_amo=False))
smatest()
    # Author  : Mahendran Paramasivan