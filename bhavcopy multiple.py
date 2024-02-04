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
for i in range(1,125):
    d = datetime.today() - timedelta(i)
    # print(d)
    # print(d.strftime("%d-%m-%Y"))
    # print(get_bhavcopy(d.strftime("%d-%m-%Y")))
# print(get_bhavcopy("13-11-2023"))
# print(get_bhavcopy("13-11-2023"))

#     print(get_bhavcopy(d.strftime("%d-%b-%Y")))

    if (d.weekday() <= 4) and (d.strftime("%d-%m-%Y") not in hd):
        prices = get_bhavcopy(d.strftime("%d-%m-%Y"))
        df = pd.DataFrame(prices)
        df1.append(df)
df1 = pd.concat(df1)
print(df1)
df1['H_L'] = df1[' HIGH_PRICE'] - df1[' LOW_PRICE']
df1['C_O'] = df1[' CLOSE_PRICE'] - df1[' OPEN_PRICE']
df2 = df1[df1[' SERIES'] == ' EQ']
# df2.pivot(df1['SYMBOL'], df1[' DATE1'], df1['C_O'])
# df2 = df1.pivot('SYMBOL',' DATE1','C_O')
# df2 = df.pivot_table(index='SYMBOL',columns=' DATE1',values=' CLOSE_PRICE')
# df2=sort_values(by='SYMBOL',ascending=True)
df2.to_csv('C:\\Users\\mahen\\OneDrive\\Documents\\Bhavcopy.csv')
print(df2)
