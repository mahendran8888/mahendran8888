import json

import pandas as pd
import requests

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                         'like Gecko) '
                         'Chrome/80.0.3987.149 Safari/537.36',
           'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}

res = requests.get("https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY", headers=headers)
df = pd.DataFrame(res)
print(df)