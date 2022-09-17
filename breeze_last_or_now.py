import pandas as pd
import xlwings as xw
import datetime
from datetime import datetime, timedelta

from breeze_connect import BreezeConnect

breeze = BreezeConnect(api_key="9493XC574494gm2E591i039Qb2(p90e1")
breeze.generate_session(api_secret="071876u)z486md346506_1256~3Q31&D", session_token="1471639")

bnquote = breeze.get_quotes(stock_code="CNXBAN",exchange_code="NFO",expiry_date="2022-08-11T06:00:00.000Z",product_type="options",right="call",strike_price="38600")

print(bnquote)
# df = pd.DataFrame(bnc['Success'])
# print(df)

