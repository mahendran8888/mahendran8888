import requests
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


class NseIndia:

    def __int__(self):
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple'
                                      'WebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
           #  ,
           # 'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
        self.session = requests.Session()
        # self.cookies = dict(requests.cookies)
        self.session.get("https://nseindia.com/", headers=self.headers)

    def pre_market_data(self, key):
        pre_market_key = {"NIFTY 50": "NIFTY","Nifty Bank":"BANKNIFTY"}
        key="NIFTY 50"
        data = self.session.get(f"https://www.nseindia.com/api/market-data-pre-open?key={pre_market_key[key]}",
                                headers=self.headers).json()["data"]
        new_data = []
        for i in data:
            new_data.append(i["metadata"])
        df = pd.DataFrame(new_data)
        return df

    def holidays(self):
        holiday = ["clearing","trading"]
        key = "trading"
        data = self.session.get(f'https://www.nseindia.com/api/holiday-master?type={holiday[holiday.index(key)]}',headers=self.headers, timeout=5, cookies=cookies).json()
        df = pd.DataFrame(list(data.values())[0])
        return df



