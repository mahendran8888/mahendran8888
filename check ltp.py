from breeze_connect import BreezeConnect
from datetime import datetime, date, time, timedelta
import pandas as pd
import numpy as np
from alice_blue import *

Login details here

quote = breeze.get_quotes(stock_code="ITC",
            exchange_code="NSE",
            expiry_date="2022-08-04T06:00:00.000Z",
            product_type="cash",
            right="others",
            strike_price="0")
# print(quote)
ohlc = pd.DataFrame(quote['Success'])
# print(ohlc)
ohlc1 = ohlc.loc[ohlc['exchange_code'] == 'NSE']
ltp = ohlc1["ltp"].iloc[0]
# ltp = pd.DataFrame(ohlc1["ltp"])
print(ltp)
print(type(ltp))
print(round(ltp*0.01,1))

print(alice.place_order(transaction_type=TransactionType.Buy,
                        instrument=alice.get_instrument_by_symbol('NSE', 'ITC'),
                        quantity=1,
                        order_type=OrderType.StopLossLimit,
                        product_type=ProductType.BracketOrder,
                        price=round(ltp,1),
                        trigger_price=round(ltp*0.01,1),
                        stop_loss=round(ltp*0.01,1),
                        square_off=round(ltp*0.01,1),
                        trailing_sl=None,
                        is_amo=False))

