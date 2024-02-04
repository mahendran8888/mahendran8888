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

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

breeze = BreezeConnect(api_key=api_key)
breeze.generate_session(api_secret=api_secret, session_token=session_token)


p=100
tp=15
sl=40
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

bnpe = breeze.get_historical_data(interval="1minute", from_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                                  to_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'), stock_code="CNXBAN", exchange_code="NFO",
                                  product_type="options",expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                                  right="put",strike_price=pestrikeprice)
dfce100 = pd.DataFrame(bnce['Success'])
# print(dfce100)
dfpe100 = pd.DataFrame(bnpe['Success'])
# print(dfpe100)

def rma(x, n, y0):
    a = (n-1) / n
    ak = a**np.arange(len(x)-1, -1, -1)
    return np.r_[np.full(n, np.nan), y0, np.cumsum(ak * x) / ak / n + y0 * a**np.arange(1, len(x)+1)]
#
dfce100['change'] = pd.to_numeric(dfce100['close']).diff()
dfce100['gain'] = dfce100.change.mask(dfce100.change < 0, 0.0)
dfce100['loss'] = -dfce100.change.mask(dfce100.change > 0, -0.0)
n = 14
dfce100['avg_gain'] = rma(dfce100.gain[n+1:].to_numpy(), n, np.nansum(dfce100.gain.to_numpy()[:n+1])/n)
dfce100['avg_loss'] = rma(dfce100.loss[n+1:].to_numpy(), n, np.nansum(dfce100.loss.to_numpy()[:n+1])/n)
dfce100['rs'] = dfce100.avg_gain / dfce100.avg_loss
dfce100['rsi_14'] = 100 - (100 / (1 + dfce100.rs))
# print(dfce100)
# dfce100['sma'] = dfce100['close'].rolling(10).mean()
dfce100['lowp'] = dfce100['low'].iloc[-2]
dfce100['highp'] = dfce100['high'].iloc[-2]
dfce100ltp = pd.to_numeric(dfce100['close'].iloc[-1])
dfceltp100tp = round(dfce100ltp * (1+tp/100), -1)
dfceltp100sl = round(dfce100ltp * (1-sl/100), -1)
dfpe100ltp = pd.to_numeric(dfpe100['close'].iloc[-1])
dfpeltp100tp = round(dfpe100ltp * (1+tp/100), -1)
dfpeltp100sl = round(dfpe100ltp * (1-sl/100), -1)

rsi14ceprev = dfce100['rsi_14'].iloc[-2]

dfce100['lowc'] = dfce100['low'].iloc[-1]
dfce100['highc'] = dfce100['high'].iloc[-1]
rsi14cecur = dfce100['rsi_14'].iloc[-1]


print(dfce100[["open","high","low","close","datetime","rsi_14"]][len(dfce100)-2:len(dfce100)])
# print(rsi14cecur,rsi14ceprev)

dfpe100['change'] = pd.to_numeric(dfpe100['close']).diff()
dfpe100['gain'] = dfpe100.change.mask(dfpe100.change < 0, 0.0)
dfpe100['loss'] = -dfpe100.change.mask(dfpe100.change > 0, -0.0)
n = 14
dfpe100['avg_gain'] = rma(dfpe100.gain[n+1:].to_numpy(), n, np.nansum(dfpe100.gain.to_numpy()[:n+1])/n)
dfpe100['avg_loss'] = rma(dfpe100.loss[n+1:].to_numpy(), n, np.nansum(dfpe100.loss.to_numpy()[:n+1])/n)
dfpe100['rs'] = dfpe100.avg_gain / dfpe100.avg_loss
dfpe100['rsi_14'] = 100 - (100 / (1 + dfpe100.rs))
# print(dfce100)
# dfce100['sma'] = dfce100['close'].rolling(10).mean()
dfpe100['lowp'] = dfpe100['low'].iloc[-2]
dfpe100['highp'] = dfpe100['high'].iloc[-2]
rsi14peprev = dfpe100['rsi_14'].iloc[-2]

dfpe100['lowc'] = dfpe100['low'].iloc[-1]
dfpe100['highc'] = dfpe100['high'].iloc[-1]
rsi14pecur = dfpe100['rsi_14'].iloc[-1]

print(dfpe100[["open","high","low","close","datetime","rsi_14"]][len(dfpe100)-2:len(dfpe100)])
print("rsi14cecur  :",rsi14cecur,"\nrsi14ceprev :",rsi14ceprev,"\nrsi14pecur  :",rsi14pecur,"\nrsi14peprev :",rsi14peprev,"\ndfce100ltp  :",dfce100ltp,"\ndfpe100ltp  :",dfpe100ltp,"\ndfceltp100tp:",dfceltp100tp,"\ndfpeltp100tp:",dfpeltp100tp,"\ndfpeltp100sl:",dfpeltp100sl,"\ndfceltp100sl:",dfceltp100sl,"\nCE-Price    :",dfce100['strike_price'][0],"\nPE-Price    :",dfpe100['strike_price'][0])

if rsi14ceprev < 30 and rsi14cecur > 30 :

    print(breeze.place_order(stock_code="CNXBAN",
                       exchange_code="NFO",
                       product="options",
                       action="buy",
                       order_type="market",
                       stoploss=dfpeltp100sl,
                       quantity="25",
                       price="",
                       validity="day",
                       validity_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                       disclosed_quantity="25",
                       expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                       right="call",
                       strike_price=cestrikeprice))

    print(breeze.place_order(stock_code="CNXBAN",
                       exchange_code="NFO",
                       product="options",
                       action="sell",
                       order_type="limit",
                       stoploss="",
                       quantity="25",
                       price=dfceltp100tp,
                       validity="day",
                       validity_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                       disclosed_quantity="25",
                       expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                       right="call",
                       strike_price=cestrikeprice))


if rsi14peprev < 30 and rsi14pecur > 30:

    print(breeze.place_order(stock_code="CNXBAN",
                       exchange_code="NFO",
                       product="options",
                       action="buy",
                       order_type="market",
                       stoploss=dfpeltp100sl,
                       quantity="25",
                       price="",
                       validity="day",
                       validity_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                       disclosed_quantity="0",
                       expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                       right="put",
                       strike_price=pestrikeprice))

    print(breeze.place_order(stock_code="CNXBAN",
                       exchange_code="NFO",
                       product="options",
                       action="sell",
                       order_type="limit",
                       stoploss="",
                       quantity="25",
                       price=dfpeltp100tp,
                       validity="day",
                       validity_date=datetime.now().strftime('%Y-%m-%dT06:00:00.000Z'),
                       disclosed_quantity="25",
                       expiry_date=currentExpiry.strftime('%Y-%m-%dT06:00:00.000Z'),
                       right="put",
                       strike_price=pestrikeprice))
t2=time.time()
print(t2-t1)