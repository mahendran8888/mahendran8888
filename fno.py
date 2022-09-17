import requests
import pandas as pd
import numpy
import pprint
import json
from pandas.io.json import json_normalize
import xlwings as xw
import win32com.client
url = 'https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple'
                              'WebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
                              'accept-language': 'en,gu;q=0.9,hi;q=0.8',
                              'accept-encoding': 'gzip, deflate, br'}
session = requests.Session()
requests = session.get(url, headers=headers)
cookies = dict(requests.cookies)
requests = session.get(url, headers=headers,cookies=cookies).json()

print(requests)
df = json_normalize(requests)
print(df)

wb = xw.Book('C:\\Users\\mahen\\OneDrive\\Desktop\\Test1.xlsx')
# wb.api.RefreshAll()
sht1 = wb.sheets['Sheet1']
xw.Range('A1').value = df = df
xw.Range('A1').options(pd.DataFrame, expand='table').value