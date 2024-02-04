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
from Indicators001 import *
t1=time.time()
requests.packages.urllib3.util.connection.HAS_IPV6 = False

if (datetime.today().weekday() == 3):
    currentExpiry = nse_expirydetails(nse_optionchain_scrapper('BANKNIFTY'), 1)[0]
else:
    currentExpiry = nse_expirydetails(nse_optionchain_scrapper('BANKNIFTY'), 0)[0]

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

breeze = BreezeConnect(api_key=api_key)
breeze.generate_session(api_secret=api_secret, session_token=session_token)


p=50
t=10
sl=50
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
dfcep = pd.DataFrame(bnce['Success'])
dfpep = pd.DataFrame(bnpe['Success'])
# print(dfce100,dfpe100)

# indicator
# dfce_rsi = rsi01(dfcep)['rsi_14']
# dfpe_rsi = rsi01(dfpep)['rsi_14']
dfce_rsip = rsi01(dfcep)['rsi_14'].iloc[-2]
dfpe_rsip = rsi01(dfpep)['rsi_14'].iloc[-2]
dfce_rsic = rsi01(dfcep)['rsi_14'].iloc[-1]
dfpe_rsic = rsi01(dfpep)['rsi_14'].iloc[-1]
# print(dfcersi,dfcersi)

detail = breeze.get_order_list(exchange_code="NFO",
                        from_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                        to_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'))
# detail = breeze.get_order_list(exchange_code="NFO",
#                         from_date="2023-11-23T18:00:00.000Z",
#                         to_date="2023-11-23T18:00:00.000Z")
# strikeprice_bought = pd.DataFrame(detail)['Success'][0]['strike_price']
# print(strikeprice_bought)
order_detail = pd.DataFrame(detail['Success'])
# order_detail['price+action'] = order_detail['strike_price'].map(str) + order_detail['right']
# print(order_detail)

# if order detail empty trigger first order
if order_detail.empty == True:
    if dfce_rsip < 30 and dfce_rsic > 30:
        # print(cestrikeprice)
        print(breeze.place_order(stock_code="CNXBAN",
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
                           strike_price=cestrikeprice))
    if dfpe_rsip < 30 and dfpe_rsic > 30:
        # print(pestrikeprice)
        print(breeze.place_order(stock_code="CNXBAN",
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
                           strike_price=pestrikeprice))

# if order detail have only one order, trigger sell order for buy order
elif order_detail.empty == False:
    if len(order_detail) == 1:
        single_order_id = order_detail['order_id']
        single_order_strike_price = order_detail['strike_price']
        single_order_price = order_detail['price']
        single_order_avg_price = order_detail['average_price']
        single_order_right = order_detail['right']

        if float(single_order_price) > (float(single_order_avg_price) * (100+ p / 100)):
            print(breeze.place_order(stock_code="CNXBAN",
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
                                     right=single_order_right,
                                     strike_price=single_order_strike_price,
                                     user_remark=single_order_id))


# if order detail have more than one order then
    if len(order_detail) > 1:
        buy_order_detail = order_detail[order_detail['action'].str.contains('Buy')]
        sell_order_detail = order_detail[order_detail['action'].str.contains('Sell')]

        unique_order_id = pd.concat([buy_order_detail['order_id'],sell_order_detail['user_remark']]).drop_duplicates(keep=False)
        # print(unique_order_id)
        running_order = buy_order_detail['order_id'].isin(unique_order_id)
        # print(running_order)
        running_order_row = buy_order_detail[running_order]
        # print(running_order_row)
        running_order_avg_price = running_order_row['average_price'].values
        running_order_right = running_order_row['right']
        running_order_price = running_order_row['price'].values
        running_order_strike_price = running_order_row['strike_price']
        # print(running_order_avg_price)

        if running_order_row.empty == True and dfce_rsip < 30 and dfce_rsic > 30:
            # print(cestrikeprice)
            print(breeze.place_order(stock_code="CNXBAN",
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
                               strike_price=cestrikeprice))
        if running_order_row.empty == True and dfpe_rsip < 30 and dfpe_rsic > 30:
            # print(pestrikeprice)
            print(breeze.place_order(stock_code="CNXBAN",
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
                               strike_price=pestrikeprice))

        if running_order_row.empty == False and float(running_order_price[0]) > (float(running_order_avg_price[0]) * (100+(p/100))) and running_order_right == 'call':
            print(breeze.place_order(stock_code="CNXBAN",
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
                               strike_price=running_order_strike_price,
                               user_remark=unique_order_id))

        if running_order_row.empty == False and float(running_order_price[0]) > (float(running_order_avg_price[0]) * (100+(p/100))) and running_order_right == 'put':
            print(breeze.place_order(stock_code="CNXBAN",
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
                               strike_price=running_order_strike_price,
                               user_remark=unique_order_id))


