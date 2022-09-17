import requests
import pandas as pd
import numpy
# url = 'https://www.nseindia.com/api/allIndices'
url = 'https://www.nseindia.com/api/quote-derivative?symbol=BANKNIFTY'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple'
                              'WebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
                              'accept-language': 'en,gu;q=0.9,hi;q=0.8',
                              'accept-encoding': 'gzip, deflate, br'}
session = requests.Session()
requests = session.get(url, headers=headers)
cookies = dict(requests.cookies)
requests = session.get(url, headers=headers,cookies=cookies).json()
print(requests)
df = pd.DataFrame(requests)
df1 = pd.DataFrame(df).fillna(0)
print(df1)


