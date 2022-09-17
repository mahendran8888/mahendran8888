import requests, json
import dateutil.parser
import pandas as pd
from alice_blue import *
from datetime import datetime,date,time,timedelta

Login details here

print(alice.get_trade_book())

print(alice.get_balance()) # get balance / margin limits
print(alice.get_profile()) # get profile
print(alice.get_daywise_positions()) # get daywise positions
print(alice.get_netwise_positions()) # get netwise positions
print(alice.get_holding_positions()) # get holding positions
