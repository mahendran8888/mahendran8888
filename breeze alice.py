def smatest():
    from breeze_connect import BreezeConnect
    from datetime import datetime,date,time,timedelta
    import pandas as pd
    import numpy as np
    from alice_blue import *

    access_token = AliceBlue.login_and_get_access_token(username='AB133347', password='pragati@3', twoFA='1985',
                                                        api_secret='bb4azbDnhxfJ7bbTKfd4gWjN8yc3IOXLykCLOfqvrdU3ixAONzyqe6dT0qh4xaeZ',
                                                        app_id='jvbqTE5sF8')
    alice = AliceBlue(username='AB133347', password='pragati@3', access_token=access_token)

    breeze = BreezeConnect(api_key="8*r19x1L8~YkO4807R`u7H103766JBn4")
    breeze.generate_session(api_secret="qoV%5l8L8e9&5833924d5Z469*W20PV4", session_token="1481046")

    # bnhistory = breeze.get_historical_data(interval="1minute", from_date="2022-08-08T07:00:00.000Z",
    #                                        to_date="2022-08-08T18:00:00.000Z", stock_code="CNXBAN",
    #                                        exchange_code="NFO", product_type="options",
    #                                        expiry_date="2022-08-11T18:00:00.000Z",
    #                                        right="call",strike_price=38600)
    bnhistory = breeze.get_historical_data(interval="1minute",from_date="2022-8-1T07:00:00.000Z",
                                           to_date="2022-8-8T18:00:00.000Z",stock_code="ITC",
                                           exchange_code="NSE",product_type="others")
    #                            ,
    #                            expiry_date="2021-11-25T07:00:00.000Z",
    #                            right="others",
    #                            strike_price="0")

    sma = pd.DataFrame(bnhistory['Success'])
    # print(sma)
    sma['sma_20'] = sma['close'].rolling(10).mean()
    #low
    low = sma['low'].iloc[-1]
    lowp = sma['low'].iloc[-2]
    #high
    high = sma['high'].iloc[-1]
    highp = sma['high'].iloc[-2]
    # print(sma)
    sma20 = sma['sma_20'].iloc[-1]
    sma20p = sma['sma_20'].iloc[-2]
    # print(sma20,sma20p,low,lowp,high,highp)

    if sma20 < pd.to_numeric(low) and sma20p > pd.to_numeric(lowp):
        print("Buy",sma['close'].iloc[-1])
    if sma20 > pd.to_numeric(high) and sma20p < pd.to_numeric(highp):
        print("Sell",sma['close'].iloc[-1])


smatest()
    # Author  : Mahendran Paramasivan