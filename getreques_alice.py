import requests, json
import dateutil.parser
import pandas as pd
from alice_blue import *
from datetime import datetime,date,time,timedelta

access_token = AliceBlue.login_and_get_access_token(username=', twoFA='1985', api_secret='bb4azbDnhxfJ7bbTKfd4gWjN8yc3IOXLykCLOfqvrdU3ixAONzyqe6dT0qh4xaeZ', app_id='jvbqTE5sF8')
alice = AliceBlue(username=', access_token=access_token)

lst = requests.get("https: // ant.aliceblueonline.com / api / v1 / charts / tdv?exchange = NSE & token = 1594 & candletype = 1 & starttime = 1658082600 & endtime = 1660028148 & data_duration = 15")

print(lst)
