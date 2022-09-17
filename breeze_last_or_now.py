import pandas as pd
import xlwings as xw
import datetime
from datetime import datetime, timedelta

from breeze_connect import BreezeConnect
Login details here

bnquote = breeze.get_quotes(stock_code="CNXBAN",exchange_code="NFO",expiry_date="2022-08-11T06:00:00.000Z",product_type="options",right="call",strike_price="38600")

print(bnquote)
# df = pd.DataFrame(bnc['Success'])
# print(df)

