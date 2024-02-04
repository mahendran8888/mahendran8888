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
def tsl_ce_pe():
    from breeze_connect import BreezeConnect
    from datetime import datetime,date,time,timedelta
    import pandas as pd
    import numpy as np
    # from credentials001 import *
    import requests
    import datetime
    import time
    import json
    # from nsepython import *
    from datetime import datetime
    t1=time.time()
    requests.packages.urllib3.util.connection.HAS_IPV6 = False

    holidays = pd.DataFrame(nse_holidays("trading")['CBM'])
    hd = holidays['tradingDate'].to_list()

    day = datetime.now().date()

    if day <= date(2023, 9,6):
        date1 = day + timedelta(7-((day.weekday()-3 + 7) if day.weekday()-3<0 else day.weekday()-3))
    else:
        date1 = day + timedelta(7-((day.weekday()-2 + 7) if day.weekday()-2<0 else day.weekday()-2))
    # print(day,(date1 - timedelta(days=1)) if date1.strftime("%d-%b-%Y") in hd else date1,day.weekday(),date1.weekday())
    currentExpiry = (date1 - timedelta(days=1)) if date1.strftime("%d-%b-%Y") in hd else date1
    # print("Current Expiry:",currentExpiry)

    # if datetime.today().weekday() == 2:
    #     currentExpiry = nse_expirydetails(nse_optionchain_scrapper('BANKNIFTY'), 0)[0] + timedelta(days=7)
    # else:
    #     currentExpiry = nse_expirydetails(nse_optionchain_scrapper('BANKNIFTY'), 0)[0]


    # currentExpiry = nse_expirydetails(nse_optionchain_scrapper('BANKNIFTY'), 0)[0]
    # print(currentExpiry)

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    breeze = BreezeConnect(api_key=api_key)
    breeze.generate_session(api_secret=api_secret, session_token=session_token)

    # m = 1000
    # tp = round(m/15,-2)
    # tp1 = m / 15
    # p = round(tp/4,-2)
    # p1 = round(tp1 / 4, 0)
    # print(p, tp)
    # print(p1, tp1)
    p=200
    tp=100

    df = breeze.get_option_chain_quotes(stock_code="CNXBAN",
                                        exchange_code="NFO",
                                        product_type="options",
                                        # expiry_date="2022-10-20T18:00:00.000Z",
                                        expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                                        right="call",
                                        strike_price="")
    # print(opt)
    dfce = pd.DataFrame(df['Success'])
    # print(dfce)

    dfce['sq.ltp'] = (dfce['ltp'] - p) * (dfce['ltp'] - p)
    # print(df1)
    dfce['sq.ltp.min'] = dfce['sq.ltp'].min()
    cestrikeprice = dfce.loc[dfce['sq.ltp'] == dfce['sq.ltp.min'], 'strike_price'].to_string(index=False)
    ltpce100 = dfce.loc[dfce['sq.ltp'] == dfce['sq.ltp.min'], 'ltp'].to_string(index=False)
    print(ltpce100, cestrikeprice)

    df = breeze.get_option_chain_quotes(stock_code="CNXBAN",
                                        exchange_code="NFO",
                                        product_type="options",
                                        # expiry_date="2022-10-20T18:00:00.000Z",
                                        expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                                        right="put",
                                        strike_price="")
    # print(opt)
    dfpe = pd.DataFrame(df['Success'])
    # print(dfpe)

    dfpe['sq.ltp'] = (dfpe['ltp'] - p) * (dfpe['ltp'] - p)
    # print(df1)
    dfpe['sq.ltp.min'] = dfpe['sq.ltp'].min()
    pestrikeprice = dfpe.loc[dfpe['sq.ltp'] == dfpe['sq.ltp.min'], 'strike_price'].to_string(index=False)
    ltppe100 = dfpe.loc[dfpe['sq.ltp'] == dfpe['sq.ltp.min'], 'ltp'].to_string(index=False)
    print(ltppe100, pestrikeprice)

    bnce = breeze.get_historical_data(interval="1minute", from_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                      to_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'), stock_code="CNXBAN",
                                      exchange_code="NFO",
                                      product_type="options",
                                      expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                                      right="call", strike_price=cestrikeprice)

    # bnce = breeze.get_historical_data(interval="1minute", from_date="2023-11-23T18:00:00.000Z",
    #                                   to_date="2023-11-24T18:00:00.000Z", stock_code="CNXBAN", exchange_code="NFO",
    #                                   product_type="options",expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
    #                                   right="call",strike_price=cestrikeprice)

    bnpe = breeze.get_historical_data(interval="1minute", from_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                      to_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'), stock_code="CNXBAN",
                                      exchange_code="NFO",
                                      product_type="options",
                                      expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                                      right="put", strike_price=pestrikeprice)

    # bnpe = breeze.get_historical_data(interval="1minute", from_date="2023-11-23T18:00:00.000Z",
    #                                   to_date="2023-11-24T18:00:00.000Z", stock_code="CNXBAN", exchange_code="NFO",
    #                                   product_type="options",expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
    #                                   right="put",strike_price=pestrikeprice)
    dfce100 = pd.DataFrame(bnce['Success'])
    # print("High:",dfce100[0:16]['high'].max())
    dfpe100 = pd.DataFrame(bnpe['Success'])
    # print(dfce100['close'].iloc[-1])
    #
    # print(dfpe100['close'].iloc[-1])

    detail = breeze.get_order_list(exchange_code="NFO",
                                   from_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                   to_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'))
    # detail = breeze.get_order_list(exchange_code="NFO",
    #                         from_date="2023-11-23T18:00:00.000Z",
    #                         to_date="2023-11-24T18:00:00.000Z")

    if detail['Success'] == None and (bnce['Success'] != None or bnpe['Success'] != None):

        if (float(dfce100['close'].iloc[-1]) > float(dfce100[0:17]['high'].max())):
            ce_buy_order = breeze.place_order(stock_code="CNXBAN",
                                              exchange_code="NFO",
                                              product="options",
                                              action="buy",
                                              order_type="market",
                                              stoploss="",
                                              quantity="15",
                                              price="",
                                              validity="day",
                                              validity_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                              disclosed_quantity="0",
                                              expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                                              right="call",
                                              strike_price=cestrikeprice)
            print("LTP crossed CE 15 min high price :", ce_buy_order)

        if (float(dfpe100['close'].iloc[-1]) > float(dfpe100[0:17]['high'].max())):
            pe_buy_order = breeze.place_order(stock_code="CNXBAN",
                                              exchange_code="NFO",
                                              product="options",
                                              action="buy",
                                              order_type="market",
                                              stoploss="",
                                              quantity="15",
                                              price="",
                                              validity="day",
                                              validity_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                              disclosed_quantity="0",
                                              expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                                              right="put",
                                              strike_price=pestrikeprice)
            print("LTP crossed PE 15 min high price :", pe_buy_order)

    if detail['Success'] != None:
        detail = breeze.get_order_list(exchange_code="NFO",
                                       from_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                       to_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'))

        # detail = breeze.get_order_list(exchange_code="NFO",
        #                                from_date="2023-11-23T18:00:00.000Z",
        #                                to_date="2023-11-24T18:00:00.000Z")
        detail1 = pd.DataFrame(detail['Success'])
        print(detail1)
        ce_strike_price_bought = detail1.loc[(detail1['right'] == 'Call') & (detail1['action'] == 'Buy'), 'strike_price'].to_string(index=False)
        pe_strike_price_bought = detail1.loc[(detail1['right'] == 'Put') & (detail1['action'] == 'Buy'), 'strike_price'].to_string(index=False)

        ce_avg_price_bought = detail1.loc[(detail1['right'] == 'Call') & (detail1['action'] == 'Buy'), 'average_price'].to_string(index=False)
        pe_avg_price_bought = detail1.loc[(detail1['right'] == 'Put') & (detail1['action'] == 'Buy'), 'average_price'].to_string(index=False)
        # cetp = ce_avg_price_bought.astype(float)+tp
        # petp = pe_avg_price_bought.astype(float)+tp

        bncebought = breeze.get_historical_data(interval="1minute",
                                           from_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                           to_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                           stock_code="CNXBAN",
                                           exchange_code="NFO",
                                           product_type="options",
                                           expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                                           right="call", strike_price=ce_strike_price_bought)

        bnpebought = breeze.get_historical_data(interval="1minute",
                                           from_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                           to_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                           stock_code="CNXBAN",
                                           exchange_code="NFO",
                                           product_type="options",
                                           expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                                           right="put", strike_price=pe_strike_price_bought)

        dfce101 = pd.DataFrame(bncebought['Success'])
        # print(dfce101)
        dfpe101 = pd.DataFrame(bnpebought['Success'])
        # print("High CE:", dfpe101['high'][18:400].astype(float).max(),"Close Price",dfpe101['close'].astype(float).iloc[-1],"CE_Bought",pe_avg_price_bought,pe_avg_price_bought,ce_strike_price_bought,pe_strike_price_bought,float(pe_avg_price_bought) + tp)
        # print("Close Price",dfpe101['close'].astype(float).iloc[-1],float(pe_avg_price_bought) + tp)
        # print("Close:",dfce101['close'].astype(float).iloc[-1])
        print("Close:",dfpe101['close'].astype(float).iloc[-1])

        if any(detail1['right'].isin(['Call'])) == True:
            if (float(ce_avg_price_bought) + tp) < float(dfce101['close'].iloc[-1]):
                ce_sell_order = breeze.place_order(stock_code="CNXBAN",
                                                   exchange_code="NFO",
                                                   product="options",
                                                   action="sell",
                                                   order_type="market",
                                                   stoploss="",
                                                   quantity="15",
                                                   price="",
                                                   validity="day",
                                                   validity_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                                   disclosed_quantity="0",
                                                   expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                                                   right="call",
                                                   strike_price=ce_strike_price_bought)
                print(ce_sell_order)

        if any(detail1['right'].isin(['Put'])) == True:
            if (float(pe_avg_price_bought) + tp) < float(dfpe101['close'].iloc[-1]):
                pe_sell_order = breeze.place_order(stock_code="CNXBAN",
                                                   exchange_code="NFO",
                                                   product="options",
                                                   action="sell",
                                                   order_type="market",
                                                   stoploss="",
                                                   quantity="15",
                                                   price="",
                                                   validity="day",
                                                   validity_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                                   disclosed_quantity="0",
                                                   expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                                                   right="put",
                                                   strike_price=pe_strike_price_bought)
                print(pe_sell_order)
                # time.sleep(2)
import _datetime;
from datetime import datetime
now = _datetime.datetime.now()

minute = now.minute

while minute <= 59:
    tsl_ce_pe()
    time.sleep(60)
    minute = now.minute
# Author  : Mahendran Paramasivan
