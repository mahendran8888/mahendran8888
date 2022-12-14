from breeze_connect import BreezeConnect
from datetime import datetime, date, time, timedelta
import pandas as pd
import numpy as np
import datetime
import time
from alice_blue import *

Login details here

# get LTP of live NiftyBank
bn = breeze.get_quotes(stock_code="CNXBAN",
                       exchange_code="NSE",
                       expiry_date="",
                       product_type="cash",
                       right="others",
                       strike_price="0")
df = pd.DataFrame(bn['Success'])
spot_price = round(df['ltp'].loc[0], -2)

# get call option price for present strike price
bnc = breeze.get_quotes(stock_code="CNXBAN",
                        exchange_code="NFO",
                        expiry_date="2022-08-25T06:00:00.000Z",
                        product_type="options",
                        right="call",
                        strike_price=spot_price)
# print(bnc)
df = pd.DataFrame(bnc['Success'])
call_price = df['ltp'].loc[0]
# print(call_price)

# get put option price for present strike price
bnp = breeze.get_quotes(stock_code="CNXBAN",
                        exchange_code="NFO",
                        expiry_date="2022-08-25T06:00:00.000Z",
                        product_type="options",
                        right="put",
                        strike_price=spot_price)
# print(bnp)
df = pd.DataFrame(bnp['Success'])
put_price = df['ltp'].loc[0]
# print(put_price)

# Place Call - buy order
print(alice.place_order(transaction_type = TransactionType.Buy,
                 instrument = alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2022, 8, 25), is_fut=False, strike=spot_price, is_CE = True),
                 quantity = 25,
                 order_type = OrderType.StopLossLimit,
                 product_type = ProductType.Intraday,
                 price = call_price,
                 trigger_price = None,
                 stop_loss = 25.0,
                 square_off = 100.0,
                 trailing_sl = None,
                 is_amo = False))

# place Put - buy Order
print(alice.place_order(transaction_type = TransactionType.Buy,
                 instrument = alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2022, 8, 25), is_fut=False, strike=spot_price, is_CE = False),
                 quantity = 25,
                 order_type = OrderType.StopLossLimit,
                 product_type = ProductType.Intraday,
                 price = put_price,
                 trigger_price = None,
                 stop_loss = 25.0,
                 square_off = 100.0,
                 trailing_sl = None,
                 is_amo = False))
