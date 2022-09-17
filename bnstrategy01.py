from breeze_connect import BreezeConnect
from datetime import datetime,date,time,timedelta
import pandas as pd
import numpy as np

# login

breeze = BreezeConnect(api_key="1W8960859342@I0rg534r7K^~9P92H_0")
breeze.generate_session(api_secret="69498407bAQ13a90IJ3^66s35pj626Z4", session_token="1476148")

bn = breeze.get_quotes(stock_code="CNXBAN",
                       exchange_code="NSE",
                       expiry_date="2022-08-11T06:00:00.000Z",
                       product_type="cash",
                       right="others",
                       strike_price="0")
df = pd.DataFrame(bn['Success'])
actual_ltp = df[df['exchange_code'] == 'NSE']['ltp']
# print(actual_ltp)
rounded_ltp = round(actual_ltp, -2).to_string(index=False)
rounded_ltp = pd.to_numeric(rounded_ltp).astype(int)
# print(rounded_ltp)


# Call - Premium of 100 - Strikeprice
df1=[]
for i in range(rounded_ltp + 500, rounded_ltp + 1000, 100):
    bnc = breeze.get_quotes(stock_code="CNXBAN",
                            exchange_code="NFO",
                            expiry_date="2022-08-11T06:00:00.000Z",
                            product_type="options",
                            right="call",
                            strike_price=i)

    df = pd.DataFrame(bnc['Success'])
    # print(df)
    df1.append(df)
df1 = pd.concat(df1)
df1['sq.ltp'] = (df1['ltp'] - 100) * (df1['ltp'] - 100)
# print(df1)
df1['sq.ltp.min']=df1['sq.ltp'].min()
strikeprice100 = df1.loc[df1['sq.ltp'] == df1['sq.ltp.min'], 'strike_price'].to_string(index=False)
# print(strikeprice100)

#SMA 20 Strategy used here
bnhistory = breeze.get_historical_data(interval="1minute", from_date="2022-08-05T07:00:00.000Z", to_date="2022-08-05T18:00:00.000Z", stock_code="CNXBAN", exchange_code="NFO", product_type="options",expiry_date="2022-08-11T18:00:00.000Z",right="call",strike_price=strikeprice100)
bnquote = breeze.get_quotes(stock_code="CNXBAN",exchange_code="NFO",expiry_date="2022-08-11T06:00:00.000Z",product_type="options",right="call",strike_price=strikeprice100)
sma = pd.DataFrame(bnhistory['Success'])
# print(sma)
sma['sma_20'] = sma['close'].rolling(20).mean()
sma20trigger = sma['sma_20'].iloc[-1]
print(sma['close'].iloc[-1])
print(sma20trigger)
print("sma1 : ",sma['sma_20'].iloc[-1])
print("sma2 : ",sma['sma_20'].iloc[-2])
ltp=pd.DataFrame(bnquote['Success'])
ltp100=ltp['ltp'].to_list()
print(ltp100)
if ltp100 > sma20trigger and sma['sma_20'].iloc[-2] > pd.to_numeric(sma['close'].iloc[-2]):
    print("Buy")

# sma.to_csv('C:\\Users\\mahen\\OneDrive\\Desktop\\Test123456.csv')
    # Place an order from your account.
    # breeze.place_order(stock_code="CNXBAN",
    #                    exchange_code="NFO",
    #                    product="options",
    #                    action="buy",
    #                    order_type="market",
    #                    stoploss="0",
    #                    quantity="25",
    #                    price="",
    #                    validity="day",
    #                    validity_date="",
    #                    disclosed_quantity="0",
    #                    expiry_date="2022-08-11T06:00:00.000Z",
    #                    right="call",
    #                    strike_price=strikeprice100,
    #                    user_remark="Algo Works Perfectly, SMA 20 gives Signal to Buy")