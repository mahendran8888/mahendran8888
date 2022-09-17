import requests, json
import dateutil.parser
import pandas as pd
from alice_blue import *
from datetime import datetime,date,time,timedelta

access_token = AliceBlue.login_and_get_access_token(username='AB133347', password='pragati@3', twoFA='1985', api_secret='bb4azbDnhxfJ7bbTKfd4gWjN8yc3IOXLykCLOfqvrdU3ixAONzyqe6dT0qh4xaeZ', app_id='jvbqTE5sF8')
alice = AliceBlue(username='AB133347', password='pragati@3', access_token=access_token)

def get_historical(instrument, from_datetime, to_datetime, interval, indices=False):
    params = {"token": instrument.token,
              "exchange": instrument.exchange if not indices else "NSE_INDICES",
              "starttime": str(int(from_datetime.timestamp())),
              "endtime": str(int(to_datetime.timestamp())),
              "candletype": 3 if interval.upper() == "DAY" else (2 if interval.upper().split("_")[1] == "HR" else 1),
              "data_duration": None if interval.upper() == "DAY" else interval.split("_")[0]}
    lst = requests.get( f" ant.aliceblueonline.com/api/v1/charts/tdv?",params=params).json()["data"]["candles"]

    # https: // ant.aliceblueonline.com / api / v1 / charts / tdv?exchange = BSE_INDICES & token = 1 & candletype = 1 & starttime = 1658169000 & endtime = 1660022552 & data_duration = 1
    # https: // ant.aliceblueonline.com / api / v1 / charts / tdv?exchange = NSE_INDICES & token = 26000 & candletype = 1 & starttime = 1658169000 & endtime = 1660022622 & data_duration = 1
    # https: // ant.aliceblueonline.com / api / v1 / charts / tdv?exchange = NSE_INDICES & token = 26000 & candletype = 1 & starttime = 1658082600 & endtime = 1660022677 & data_duration = 10
    # https: // ant.aliceblueonline.com / api / v1 / charts / tdv?exchange = NSE & token = 1594 & candletype = 1 & starttime = 1658082600 & endtime = 1660028148 & data_duration = 15
    records = []
    for i in lst:
        record = {"date": dateutil.parser.parse(i[0]), "open": i[1], "high": i[2], "low": i[3], "close": i[4], "volume": i[5]}
        records.append(record)
    return records


instrument =  alice.get_instrument_by_symbol("NSE", "ITC")
from_datetime = datetime.now() - timedelta(days=10)
to_datetime = datetime.now()
interval = "1_MIN" # ["DAY", "1_HR", "3_HR", "1_MIN", "5_MIN", "15_MIN", "60_MIN"]
indices = True

df = pd.DataFrame(get_historical(instrument, from_datetime, to_datetime, interval, indices))
df.index = df["date"]
df = df.drop("date", axis=1)
df["MA_10"] = df["close"].rolling(window=10).mean()
print(df)

