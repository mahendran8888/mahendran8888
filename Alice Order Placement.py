from breeze_connect import BreezeConnect
from datetime import datetime, date, time, timedelta
import pandas as pd
import numpy as np
import datetime
import time
from alice_blue import *

# breeze = BreezeConnect(api_key="")
# breeze.generate_session(api_secret="", session_token="")

access_token = AliceBlue.login_and_get_access_token(username='', password='', twoFA='',
                                                    api_secret='',
                                                    app_id='')
alice = AliceBlue(username='AB133347', password='pragati@3', access_token=access_token)

print(alice.place_order(transaction_type=TransactionType.Buy,
                      instrument=alice.get_instrument_by_symbol('NSE', "TATASTEEL"),
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


