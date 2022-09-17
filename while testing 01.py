from breeze_connect import BreezeConnect
from datetime import datetime, date, time, timedelta
import pandas as pd
import numpy as np
import datetime
import time
from alice_blue import *
import stoplose_takeprofit
import xlwings as xw

Login details here

now = datetime.datetime.now()

minute = now.minute

while minute <= 59:
    stoplose_takeprofit
    # print(datetime.datetime.now())
    time.sleep(1)
    minute = now.minute
    wb = xw.Book('C:\\Users\\mahen\\OneDrive\\Desktop\\takeprofit.csv')
    # wb.api.RefreshAll()
    sht1 = wb.sheets['Sheet1']
    xw.Range('A1').value = df = trade_log
    xw.Range('A1').options(pd.DataFrame, expand='table').value
# Author  : Mahendran Paramasivan
