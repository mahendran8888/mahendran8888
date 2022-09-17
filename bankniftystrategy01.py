from breeze_connect import BreezeConnect
from datetime import datetime,date,time,timedelta
from nsepy import get_history
import pandas as pd
import numpy as np
Login details here
bn=breeze.get_quotes(stock_code="CNXBAN",
                    exchange_code="NSE",
                    expiry_date="2022-08-05T06:00:00.000Z",
                    product_type="cash",
                    right="others",
                    strike_price="0")
df = pd.DataFrame(bn['Success'])
actual_ltp =df[df['exchange_code'] == 'NSE']['ltp']
rounded_ltp=round(actual_ltp, -2).to_string(index=False)
rounded_ltp=pd.to_numeric(rounded_ltp).astype(int)
