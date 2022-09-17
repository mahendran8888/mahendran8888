# import requests, json
# import dateutil.parser
# import pandas as pd
# from alice_blue import *
# from datetime import datetime,date,time,timedelta
#
# access_token = AliceBlue.login_and_get_access_token(username='685531', password='Sw0rdfi$h2414', twoFA='1985', api_secret='4ErPaMZUflVgSSx1Hdns8h0NUBpHzjGCip60xz9SMjSa4sN9opTkW0AtV8o76rLXZsRK2dv8khLxRprXp7ACllHN36a548NljRyCrtDeuc1f9Ott1hWcvyrlCIqEFu03', app_id='')
# alice = AliceBlue(username='685531', password='Sw0rdfi$h2414', access_token=access_token)
#
# print(alice.get_trade_book())
#
# print(alice.get_balance()) # get balance / margin limits
# print(alice.get_profile()) # get profile
# print(alice.get_daywise_positions()) # get daywise positions
# print(alice.get_netwise_positions()) # get netwise positions
# print(alice.get_holding_positions()) # get holding positions

from datetime import datetime
from datetime import timedelta
from alice_blue import *
from pya3 import *
from datetime import datetime, date, time, timedelta

alice = Aliceblue(user_id='685531',api_key='4ErPaMZUflVgSSx1Hdns8h0NUBpHzjGCip60xz9SMjSa4sN9opTkW0AtV8o76rLXZsRK2dv8khLxRprXp7ACllHN36a548NljRyCrtDeuc1f9Ott1hWcvyrlCIqEFu03')

print(alice.get_session_id()) # Get Session ID

# instrument = alice.get_instrument_by_symbol("NFO", "RELIANCE")
# from_datetime = datetime.now() - datetime.timedelta(days=7)     # From last & days
# to_datetime = datetime.now()                                    # To now
# interval = "15"       # ["1", "2", "3", "4", "5", "10", "15", "30", "60", "120", "180", "240", "D", "1W", "1M"]
# indices = False      # For Getting index data
# # print(alice.get_historical(instrument, from_datetime, to_datetime, interval, indices))
print(alice.get_historical(alice.get_instrument_by_symbol("NFO", "ITC"), datetime(2022,8,26), datetime(2022,8,26), "5", False))


print(alice.place_order(transaction_type=TransactionType.Buy,
                      instrument=alice.get_instrument_by_symbol('NSE', "ITC"),
                      quantity=1,
                      order_type=OrderType.StopLossLimit,
                      product_type=ProductType.BracketOrder,
                      price=3.0,
                      trigger_price=3.0,
                      stop_loss=2.0,
                      square_off=2.0,
                      trailing_sl=1,
                      is_amo=False)
)