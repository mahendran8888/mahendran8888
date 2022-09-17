import requests
import dateutil.parser
from datetime import datetime, timedelta
import pandas as pd
from alice_blue import *
from config import Credentials
import datetime
import os os.environ['WDM_LOG_LEVEL'] = '0'

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

SCRIPT_LIST = ['SBIN', 'HDFC', 'IOC', 'CADILAHC', 'BATAINDIA', 'ITC', 'DABUR', 'BIOCON', 'ESCORTS', 'LUPIN','LTI']
CDS_SCRIPT_LIST = ['USDINR FEB FUT']
MCX_SCRIPT_LIST = ['SILVERM AUG FUT','CRUDEOIL AUG FUT']

socket_opened = False

def event_handler_quote_update(message):
    ltp = message['ltp']
    timestamp = datetime.datetime.fromtimestamp(message['exchange_time_stamp'])
    vol = message['volume'] instrumnet = message['instrument'].symbol
    exchange = message['instrument'].exchange
    high = message['high']
    low = message['low']

def open_callback():
    global socket_opened
    socket_opened = True
    print("Socket opened")

def login():
    access_token = AliceBlue.login_and_get_access_token(username=Credentials.UserName.value,
                                                        password=Credentials.PassWord.value,
                                                        twoFA=Credentials.twoFA.value,
                                                        api_secret=Credentials.SecretKey.value,
                                                        app_id=Credentials.AppId.value)
    alice = AliceBlue(username=Credentials.UserName.value, password=Credentials.PassWord.value,
                      access_token=access_token, master_contracts_to_download=['MCX', 'NSE', 'CDS'])
    alice.start_websocket(subscribe_callback=event_handler_quote_update, socket_open_callback=open_callback, run_in_background=True)
    while (socket_opened == False):
        pass
    for script in SCRIPT_LIST:
        alice.subscribe(alice.get_instrument_by_symbol('NSE', script), LiveFeedType.MARKET_DATA)
    for script in CDS_SCRIPT_LIST:
        alice.subscribe(alice.get_instrument_by_symbol('CDS', script), LiveFeedType.MARKET_DATA)
    for script in MCX_SCRIPT_LIST:
        print(script) alice.subscribe(alice.get_instrument_by_symbol( 'MCX', script), LiveFeedType.MARKET_DATA)
    return alice

def get_historical(instrument, from_datetime, to_datetime, interval, indices=False):
    params = {"token": instrument.token,
              "exchange": instrument.exchange if not indices else "NSE_INDICES",
              "starttime": str(int(from_datetime.timestamp())),
              "endtime": str(int(to_datetime.timestamp())),
              "candletype": 3 if interval.upper() == "DAY" else (2 if interval.upper().split("_")[1] == "HR" else 1),
              "data_duration": None if interval.upper() == "DAY" else interval.split("_")[0]}
    lst = requests.get( f" ant.aliceblueonline.com/api/v1/charts/tdv?",params=params).json()["data"]["candles"]
    records = []
    for i in lst:
        record = {"date": dateutil.parser.parse(i[0]), "open": i[1], "high": i[2], "low": i[3], "close": i[4], "volume": i[5]}
        records.append(record)
    return records
    if _name_ == '__main__':
    alice = login()
    from_datetime = datetime.datetime.now() - timedelta(days=10)
    to_datetime = datetime.datetime.now()
    interval = "5_MIN" # ["DAY", "1_HR", "3_HR", "1_MIN", "5_MIN", "15_MIN", "60_MIN"]
    indices = False
    for script in MCX_SCRIPT_LIST:
        print(script)
    instrument = alice.get_instrument_by_symbol("MCX", script)
    df = pd.DataFrame(get_historical(instrument, from_datetime, to_datetime, interval, indices))
    df.index = df["date"]
    df = df.drop("date", axis=1)
    df["MA_10"] = df["close"].rolling(window=10).mean()
    print(df)