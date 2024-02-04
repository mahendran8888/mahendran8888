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


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

breeze = BreezeConnect(api_key=api_key)
breeze.generate_session(api_secret=api_secret, session_token=session_token)

stock = breeze.get_historical_data(interval="1minute",
                                       from_date="2022-10-14T07:00:00.000Z",
                                       to_date="2022-10-14T18:00:00.000Z",
                                       stock_code="ITC",
                                       exchange_code="NSE",
                                       product_type="others")
data = pd.DataFrame(stock['Success'])
# print(data)

data['tr0'] = abs(pd.to_numeric(data["high"]) - pd.to_numeric(data["low"]))

data['tr1'] = abs(pd.to_numeric(data["high"]) - pd.to_numeric(data["close"]).shift(1))
data['tr2'] = abs(pd.to_numeric(data["low"])- pd.to_numeric(data["close"]).shift(1))
data["TR"] = round(data[['tr0', 'tr1', 'tr2']].max(axis=1),2)
data["ATR"]=0.00
data['BUB']=0.00
data["BLB"]=0.00
data["FUB"]=0.00
data["FLB"]=0.00
data["ST"]=0.00

#
# Calculating ATR
for i, row in data.iterrows():
    if i == 0:
        data.loc[i,'ATR'] = 0.00#data['ATR'].iat[0]
    else:
        data.loc[i,'ATR'] = ((data.loc[i-1,'ATR'] * 13)+data.loc[i,'TR'])/14

data['BUB'] = round(((pd.to_numeric(data["high"]) + pd.to_numeric(data["low"])) / 2) + (2 * data["ATR"]),2)
data['BLB'] = round(((pd.to_numeric(data["high"]) + pd.to_numeric(data["low"])) / 2) - (2 * data["ATR"]),2)
# print(data)

# FINAL UPPERBAND = IF( (Current BASICUPPERBAND < Previous FINAL UPPERBAND) or (Previous Close > Previous FINAL UPPERBAND))
#                     THEN (Current BASIC UPPERBAND) ELSE Previous FINALUPPERBAND)


for i, row in data.iterrows():
    if i==0:
        data.loc[i,"FUB"]=0.00
    else:
        if (data.loc[i,"BUB"]<data.loc[i-1,"FUB"])|(pd.to_numeric(data.loc[i-1,"close"])>data.loc[i-1,"FUB"]):
            data.loc[i,"FUB"]=data.loc[i,"BUB"]
        else:
            data.loc[i,"FUB"]=data.loc[i-1,"FUB"]

# FINAL LOWERBAND = IF( (Current BASIC LOWERBAND > Previous FINAL LOWERBAND) or (Previous Close < Previous FINAL LOWERBAND))
#                     THEN (Current BASIC LOWERBAND) ELSE Previous FINAL LOWERBAND)

for i, row in data.iterrows():
    if i==0:
        data.loc[i,"FLB"]=0.00
    else:
        if (data.loc[i,"BLB"]>data.loc[i-1,"FLB"])|(pd.to_numeric(data.loc[i-1,"close"])<data.loc[i-1,"FLB"]):
            data.loc[i,"FLB"]=data.loc[i,"BLB"]
        else:
            data.loc[i,"FLB"]=data.loc[i-1,"FLB"]



# SUPERTREND = IF((Previous SUPERTREND = Previous FINAL UPPERBAND) and (Current Close <= Current FINAL UPPERBAND)) THEN
#                 Current FINAL UPPERBAND
#             ELSE
#                 IF((Previous SUPERTREND = Previous FINAL UPPERBAND) and (Current Close > Current FINAL UPPERBAND)) THEN
#                     Current FINAL LOWERBAND
#                 ELSE
#                     IF((Previous SUPERTREND = Previous FINAL LOWERBAND) and (Current Close >= Current FINAL LOWERBAND)) THEN
#                         Current FINAL LOWERBAND
#                     ELSE
#                         IF((Previous SUPERTREND = Previous FINAL LOWERBAND) and (Current Close < Current FINAL LOWERBAND)) THEN
#                             Current FINAL UPPERBAND


for i, row in data.iterrows():
    if i==0:
        data.loc[i,"ST"]=0.00
    elif (data.loc[i-1,"ST"]==data.loc[i-1,"FUB"]) & (pd.to_numeric(data.loc[i,"close"])<=data.loc[i,"FUB"]):
        data.loc[i,"ST"]=data.loc[i,"FUB"]
    elif (data.loc[i-1,"ST"]==data.loc[i-1,"FUB"])&(pd.to_numeric(data.loc[i,"close"])>data.loc[i,"FUB"]):
        data.loc[i,"ST"]=data.loc[i,"FLB"]
    elif (data.loc[i-1,"ST"]==data.loc[i-1,"FLB"])&(pd.to_numeric(data.loc[i,"close"])>=data.loc[i,"FLB"]):
        data.loc[i,"ST"]=data.loc[i,"FLB"]
    elif (data.loc[i-1,"ST"]==data.loc[i-1,"FLB"])&(pd.to_numeric(data.loc[i,"close"])<data.loc[i,"FLB"]):
        data.loc[i,"ST"]=data.loc[i,"FUB"]

# Buy Sell Indicator
for i, row in data.iterrows():
    if i==0:
        data["ST_BUY_SELL"]="NA"
    elif (data.loc[i,"ST"]< pd.to_numeric(data.loc[i,"close"])) :
        data.loc[i,"ST_BUY_SELL"]="BUY"
    else:
        data.loc[i,"ST_BUY_SELL"]="SELL"
print(data)