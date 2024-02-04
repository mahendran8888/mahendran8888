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

p=20

tp=10
df=breeze.get_option_chain_quotes(stock_code="CNXBAN",
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
dfce['sq.ltp.min']=dfce['sq.ltp'].min()
cestrikeprice = dfce.loc[dfce['sq.ltp'] == dfce['sq.ltp.min'], 'strike_price'].to_string(index=False)
ltpce100 = dfce.loc[dfce['sq.ltp'] == dfce['sq.ltp.min'], 'ltp'].to_string(index=False)
# print(ltpce100, cestrikeprice)

df=breeze.get_option_chain_quotes(stock_code="CNXBAN",
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
dfpe['sq.ltp.min']=dfpe['sq.ltp'].min()
pestrikeprice = dfpe.loc[dfpe['sq.ltp'] == dfpe['sq.ltp.min'], 'strike_price'].to_string(index=False)
ltppe100 = dfpe.loc[dfpe['sq.ltp'] == dfpe['sq.ltp.min'], 'ltp'].to_string(index=False)
# print(ltppe100, pestrikeprice)

bnce = breeze.get_historical_data(interval="1minute", from_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                  to_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'), stock_code="CNXBAN", exchange_code="NFO",
                                  product_type="options",expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                                  right="call",strike_price=cestrikeprice)

# bnce = breeze.get_historical_data(interval="1minute", from_date="2023-11-23T18:00:00.000Z",
#                                   to_date="2023-11-24T18:00:00.000Z", stock_code="CNXBAN", exchange_code="NFO",
#                                   product_type="options",expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
#                                   right="call",strike_price=cestrikeprice)

bnpe = breeze.get_historical_data(interval="1minute", from_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                  to_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'), stock_code="CNXBAN", exchange_code="NFO",
                                  product_type="options",expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                                  right="put",strike_price=pestrikeprice)

# bnpe = breeze.get_historical_data(interval="1minute", from_date="2023-11-23T18:00:00.000Z",
#                                   to_date="2023-11-24T18:00:00.000Z", stock_code="CNXBAN", exchange_code="NFO",
#                                   product_type="options",expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
#                                   right="put",strike_price=pestrikeprice)
dfce100 = pd.DataFrame(bnce['Success'])
# print("High:",dfce100[0:16]['high'].max())
dfpe100 = pd.DataFrame(bnpe['Success'])
print(dfce100['close'].iloc[-1])
#
print(dfpe100['close'].iloc[-1])

detail = breeze.get_order_list(exchange_code="NFO",
                               from_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                               to_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'))
# detail = breeze.get_order_list(exchange_code="NFO",
#                         from_date="2023-11-23T18:00:00.000Z",
#                         to_date="2023-11-24T18:00:00.000Z")

if detail['Success'] == None:

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

    bnce1 = breeze.get_historical_data(interval="1minute",
                                       from_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                       to_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                       stock_code="CNXBAN",
                                       exchange_code="NFO",
                                       product_type="options",
                                       expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                                       right="call", strike_price=ce_strike_price_bought)

    bnpe1 = breeze.get_historical_data(interval="1minute",
                                       from_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                       to_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                       stock_code="CNXBAN",
                                       exchange_code="NFO",
                                       product_type="options",
                                       expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                                       right="put", strike_price=pe_strike_price_bought)

    dfce101 = pd.DataFrame(bnce1['Success'])
    print("High:",dfce101['high'][18:400].max())
    dfpe101 = pd.DataFrame(bnpe1['Success'])

    if any(detail1['right'].isin(['Call'])) == True:
        if float(dfce101['high'][18:400].max()) * 0.95 < float(dfce101['close'].iloc[-1]):
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
        if float(dfpe101['high'][18:400].max()) * 0.95 < float(dfpe101['close'].iloc[-1]):
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




