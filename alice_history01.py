import requests, json
import dateutil.parser
import pandas as pd
from alice_blue import *
from datetime import datetime,date,time,timedelta

access_token = AliceBlue.login_and_get_access_token(username='AB133347', password='pragati@3', twoFA='1985', api_secret='bb4azbDnhxfJ7bbTKfd4gWjN8yc3IOXLykCLOfqvrdU3ixAONzyqe6dT0qh4xaeZ', app_id='jvbqTE5sF8')
alice = AliceBlue(username='AB133347', password='pragati@3', access_token=access_token)

print(alice.get_trade_book())

print(alice.get_balance()) # get balance / margin limits
print(alice.get_profile()) # get profile
print(alice.get_daywise_positions()) # get daywise positions
print(alice.get_netwise_positions()) # get netwise positions
print(alice.get_holding_positions()) # get holding positions
