from breeze_connect import BreezeConnect
from datetime import datetime,date,time,timedelta
import pandas as pd
import numpy as np
from credentials001 import *
import requests
import datetime
import time
from nsepython import *
from datetime import datetime
t1=time.time()
requests.packages.urllib3.util.connection.HAS_IPV6 = False
currentExpiry = nse_expirydetails(nse_optionchain_scrapper('BANKNIFTY'), 0)[0]
# print(currentExpiry)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

breeze = BreezeConnect(api_key=api_key)
breeze.generate_session(api_secret=api_secret, session_token=session_token)

df=breeze.get_historical_data(interval="1minute",
                            from_date= datetime.now().strftime('%Y-%m-%dT09:00:00.000Z'),
                            to_date= datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                            stock_code="CNXBAN",
                            exchange_code="NSE",
                            product_type="cash")
# print(pd.DataFrame(df['Success']))
close=pd.DataFrame(df['Success'])[90:91]['close'][90]
price915 = round(float(close),-2)
# print(price915)
bnce = breeze.get_historical_data(interval="1minute", from_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                  to_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'), stock_code="CNXBAN", exchange_code="NFO",
                                  product_type="options",expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                                  right="call",strike_price=price915)

# bnce = breeze.get_historical_data(interval="1minute", from_date="2023-11-23T18:00:00.000Z",
#                                   to_date="2023-11-24T18:00:00.000Z", stock_code="CNXBAN", exchange_code="NFO",
#                                   product_type="options",expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
#                                   right="call",strike_price=cestrikeprice)

bnpe = breeze.get_historical_data(interval="1minute", from_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                  to_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'), stock_code="CNXBAN", exchange_code="NFO",
                                  product_type="options",expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                                  right="put",strike_price=price915)

# bnpe = breeze.get_historical_data(interval="1minute", from_date="2023-11-23T18:00:00.000Z",
#                                   to_date="2023-11-24T18:00:00.000Z", stock_code="CNXBAN", exchange_code="NFO",
#                                   product_type="options",expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
#                                   right="put",strike_price=pestrikeprice)
dfce100 = pd.DataFrame(bnce['Success'])

dfpe100 = pd.DataFrame(bnpe['Success'])
# print(dfce100,dfpe100)

detail = breeze.get_order_list(exchange_code="NFO",
                               from_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                               to_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'))
# detail = breeze.get_order_list(exchange_code="NFO",
#                         from_date="2023-11-23T18:00:00.000Z",
#                         to_date="2023-11-24T18:00:00.000Z")

if detail['Success'] == None and (bnce['Success'] != None or bnpe['Success'] != None):

    detail = breeze.get_order_list(exchange_code="NFO",
                            from_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                            to_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'))
    detail1 = pd.DataFrame(detail['Success'])


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
                                          strike_price=price915)
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
                                          strike_price=price915)
        print("LTP crossed PE 15 min high price :", pe_buy_order)

if detail['Success'] != None:
    detail = breeze.get_order_list(exchange_code="NFO",
                            from_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                            to_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'))
    # detail = breeze.get_order_list(exchange_code="NFO",
    #                                from_date="2023-11-23T18:00:00.000Z",
    #                                to_date="2023-11-24T18:00:00.000Z")
    detail1 = pd.DataFrame(detail['Success'])
    ce_strike_price_bought = detail1.loc[detail1['right'] == 'Call', 'strike_price'].to_string(index=False)
    pe_strike_price_bought = detail1.loc[detail1['right'] == 'Put', 'strike_price'].to_string(index=False)

    if float(dfce100['high'][18:400].max())*0.95 < float(dfce100['close'].iloc[-1]) and any(detail1['right'].isin(['Call'])) == True:
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

    if float(dfpe100['high'][18:400].max())*0.95 < float(dfpe100['close'].iloc[-1]) and any(detail1['right'].isin(['Put'])) == True:
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




