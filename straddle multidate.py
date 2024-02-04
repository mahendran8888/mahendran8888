from breeze_connect import BreezeConnect
from datetime import datetime,date,time,timedelta
import pandas as pd
import numpy as np
from credentials001 import *
import requests
import datetime
import time
from nsepython import *
import json
from datetime import datetime
import itertools
from dateutil.relativedelta import relativedelta, TH
import datetime
from straddel_function001 import *
import warnings
warnings.simplefilter(action='ignore',category=FutureWarning)
holidays = pd.DataFrame(nse_holidays("trading")['CBM'])
hd = holidays['tradingDate'].to_list()
# print(hd)
# MM DD YYYY
days = pd.date_range(start='1/1/2024', end='2/2/2024')
for day in days:
    if  (day.weekday() <= 4) and (day.strftime("%d-%b-%Y") not in hd):
        # print(day.weekday(),day.strftime("%d-%b-%Y"))
        #from day, to day, Take profit and Stop lose
        straddle001(day,day,300,30)