import numpy as np
import pandas as pd
from datetime import datetime,date,time,timedelta
from nsepy import get_history
import pandas as pd
import numpy as np
import pandas_ta as ta


stocks = ['JSWSTEEL','RELIANCE','AXISBANK','HCLTECH','TECHM','HDFC','ICICIBANK','NIFTYBANK']
# stocks = ['BANKNIFTY']
# stocks = ['ADANIENT', 'ADANIPOWER', 'AMARAJABAT', 'ACC', 'RAMCOCEM', 'AMBUJACEM', 'APOLLOHOSP', 'ASIANPAINT', 'AUROPHARMA', 'AXISBANK', 'BAJAJ-AUTO', 'BAJAJFINSV', 'BAJFINANCE', 'ADANIPORTS', 'BALKRISIND', 'BHARTIARTL', 'BANDHANBNK', 'BATAINDIA', 'BEL', 'BERGEPAINT', 'BHARATFORG', 'BHEL', 'BOSCHLTD', 'BRITANNIA', 'CANBK', 'CIPLA', 'COALINDIA', 'COLPAL', 'CUMMINSIND', 'DABUR', 'BANKBARODA', 'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'EXIDEIND', 'FEDERALBNK', 'GAIL', 'GLENMARK', 'GRASIM', 'HAVELLS', 'HCLTECH', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDPETRO', 'HINDUNILVR', 'ICICIBANK', 'ICICIPRULI', 'INDIGO', 'INDUSINDBK', 'INFY', 'ITC', 'JUBLFOOD', 'JUSTDIAL', 'KOTAKBANK', 'LICHSGFIN', 'LUPIN', 'MANAPPURAM', 'MARICO', 'MARUTI', 'BIOCON', 'CADILAHC', 'MCDOWELL-N', 'MFSL', 'MGL', 'MINDTREE', 'MOTHERSUMI', 'MRF', 'MUTHOOTFIN', 'NATIONALUM', 'NCC', 'NIITTECH', 'NMDC', 'NTPC', 'PEL', 'PETRONET', 'PFC', 'PIDILITIND', 'RBLBANK', 'RECLTD', 'SAIL', 'SBIN', 'SIEMENS', 'SRF', 'SRTRANSFIN', 'SUNTV', 'TATAPOWER', 'TECHM', 'TITAN', 'TORNTPHARM', 'TORNTPOWER', 'TVSMOTOR', 'UJJIVAN', 'ULTRACEMCO', 'UPL', 'VOLTAS', 'ASHOKLEY', 'CONCOR', 'INFRATEL', 'BPCL', 'CHOLAFIN', 'DLF', 'EQUITAS', 'ESCORTS', 'IDEA', 'JSWSTEEL', 'LT', 'GODREJCP', 'GODREJPROP', 'SBILIFE', 'HDFC', 'HDFCBANK', 'IDFCFIRSTB', 'JINDALSTEL', 'M&M', 'M&MFIN', 'UBL', 'NAUKRI', 'NESTLEIND', 'ONGC', 'PAGEIND', 'POWERGRID', 'RELIANCE', 'SHREECEM', 'SUNPHARMA', 'TATAMOTORS', 'TATASTEEL', 'CENTURYTEX', 'VEDL', 'APOLLOTYRE', 'PNB', 'TATACHEM', 'IGL', 'IOC', 'TATACONSUM', 'TCS', 'WIPRO', 'ZEEL', 'L&TFH', 'IBULHSGFIN', 'GMRINFRA']
start = datetime.today() - timedelta(5)
end = datetime.today()
close_price = {}
# data=[]
for tickers in stocks:
    close_price = get_history(tickers,start,end)
    # close_price = get_history(tickers,start,end,index=True)
    df = pd.DataFrame(close_price)
    # df1=data.append(df)
    print(df)


