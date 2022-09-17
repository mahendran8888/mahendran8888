from nsepy.history import get_price_list
import numpy as np
import pandas as pd
from datetime import datetime,date,time,timedelta
from nsepy import get_history
from nsepython import *
from datetime import datetime

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# print(nse_holidays("trading"))
holidays = pd.DataFrame(nse_holidays("trading")['CBM'])
hd = holidays['tradingDate'].to_list()
# print(hd)

df1 = []
for i in range(0,6):
    d = datetime.today() - timedelta(i)
    # print(d.strftime("%d-%b-%Y"))
    if (d.weekday() <= 4) and (d.strftime("%d-%b-%Y") not in hd):
        prices = get_price_list(datetime.today() - timedelta(i))
        df = pd.DataFrame(prices)
        df1.append(df)
df1 = pd.concat(df1)

# df1.sort_values(by='SYMBOL',ascending=True)
# print(df1)
# df1['H_L'] = df1['HIGH'] - df1['LOW']
# df1['C_O'] = df1['CLOSE'] - df1['OPEN']
# df1.pivot(df1['SYMBOL'], df1['CLOSE'], df1['TIMESTAMP'])
# df2 = df1.pivot('SYMBOL','TIMESTAMP','CLOSE')
print(df1)
# df2.to_csv('C:\\Users\\mahen\\OneDrive\\Documents\\Bhavcopy.csv')
