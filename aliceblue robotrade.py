from datetime import datetime, date, time, timedelta
import pandas as pd
import numpy as np
import datetime
import time
from time import sleep
from alice_blue import *
import re
from nsepython import *

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


Login details here

global strike_price
global df
strike_price = 0
socket_opened = False
def event_handler_quote_update(message):
    # print(message)
    df = pd.DataFrame(message)
    # print(df)
    strike_price1 = df['ltp'].loc[0]
    # print(strike_price1)
    strike_price = round(df['ltp'].loc[0],-2)
    # print(strike_price)
    currentExpiry = nse_expirydetails(nse_optionchain_scrapper('BANKNIFTY'), 0)[0]

    ce_row = df.loc[df['instrument'] == 'BANKNIFTY AUG 38200.0 CE']
    # print(ce_row)
    if not ce_row.empty:
        ce_ltp = ce_row['ltp'].loc[2]
        symbol = ce_row['instrument'].loc[2]
        strike_price = re.findall("[+-]?\d+\.\d+", symbol)[0]
        # print(ce_ltp)
        # print(strike_price)

    pe_row = df.loc[df['instrument'] == 'BANKNIFTY AUG 38300.0 PE']
    if not pe_row.empty:
        pe_ltp = pe_row['ltp'].loc[2]
        symbol = pe_row['instrument'].loc[2]
        strike_price = re.findall("[+-]?\d+\.\d+", symbol)[0]
        # print(pe_ltp)
        # print(strike_price)

    alice.subscribe(alice.get_instrument_for_fno(symbol='BANKNIFTY', expiry_date=currentExpiry, is_fut=False,
                                             strike=strike_price, is_CE=True), LiveFeedType.COMPACT)

    alice.subscribe(alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=currentExpiry, is_fut=False,
                                                         strike=strike_price, is_CE = False), LiveFeedType.COMPACT)

def open_callback():
    global socket_opened
    socket_opened = True

alice.start_websocket(subscribe_callback=event_handler_quote_update,
                      socket_open_callback=open_callback,
                      run_in_background=True)
while(socket_opened==False):
    pass
    alice.subscribe(alice.get_instrument_by_symbol('NSE', 'Nifty Bank'), LiveFeedType.COMPACT)
sleep(0.7)




