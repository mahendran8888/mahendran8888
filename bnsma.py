def smatest():
    from breeze_connect import BreezeConnect
    from datetime import datetime,date,time,timedelta
    import pandas as pd
    import numpy as np
    # import breezelogin

    # breezelogin.breezelogin()
    # login
Login details here

    strikeprice = 38600

    #SMA 20 Strategy used here
    bnhistory = breeze.get_historical_data(interval="1minute", from_date="2022-09-02T07:00:00.000Z",
                                           to_date="2022-09-02T18:00:00.000Z", stock_code="CNXBAN", exchange_code="NFO",
                                           product_type="options",expiry_date="2022-09-8T18:00:00.000Z",
                                           right="call",strike_price=strikeprice)
    # print(bnhistory)
    bnquote = breeze.get_quotes(stock_code="CNXBAN",exchange_code="NFO",expiry_date="2022-9-2T06:00:00.000Z",
                                product_type="options", right="call",strike_price=strikeprice)
    sma = pd.DataFrame(bnhistory['Success'])
    # print(sma)
    sma['sma_20'] = sma['close'].rolling(20).mean()
    # print(sma)
    sma20trigger = sma['sma_20'].iloc[-1]
    sma20trigger1 = sma['sma_20'].iloc[-2]
    print("SMA20:", sma20trigger)
    # print(sma20trigger1)

    low=pd.DataFrame(bnquote['Success'])
    low100=low['low'].iloc[-1]
    print("low", low100)
    print("low-2",sma['low'].iloc[-2])
    if low100 > sma20trigger and sma['sma_20'].iloc[-2] < pd.to_numeric(sma['low'].iloc[-2]):
        print("Buy")

    high=pd.DataFrame(bnquote['Success'])
    high100=high['high'].iloc[-1]
    print("high",high100)
    print("high-2",sma['high'].iloc[-2])
    if high100 < sma20trigger and sma['sma_20'].iloc[-2] > pd.to_numeric(sma['high'].iloc[-2]):
        print("Sell")
# smatest()

# Author  : Mahendran Paramasivan
