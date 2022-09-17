from breeze_connect import BreezeConnect
from datetime import datetime,date,time,timedelta
import pandas as pd
import numpy as np
import pandas_ta as ta

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

breeze = BreezeConnect(api_key="S71P6931H176G=3#60s&4zbAmZ531730")
breeze.generate_session(api_secret="7062vS^94R16*92%9S2x4X11%wj714#2", session_token="1592984")

# stock = breeze.get_historical_data(interval="1minute",
#                                        from_date="2022-9-2T07:00:00.000Z",
#                                        to_date="2022-9-2T18:00:00.000Z",
#                                        stock_code="ITC",
#                                        exchange_code="NSE",
#                                        product_type="others")
# df = pd.DataFrame(stock['Success'])
# print(df)

data={} # Dictionary to contain pandas dataframe for all the stocks. This is to avoid creating variable for each stock
        # to store data
finalData={} # This should contain our final output and that is Renko OHLC data
n=7 # Period for ATR
renkoData={} # It contains information on the lastest bar of renko data for the number of stocks we are working on

def ATR(df,n): #df is the DataFrame, n is the period 7,14 ,etc
    df['H-L'] = abs(pd.to_numeric(df['high']) - pd.to_numeric(df['low']))
    df['H-PC'] = abs(pd.to_numeric(df['high']) - pd.to_numeric(df['close']).shift())  # high -previous close
    df['L-PC'] = abs(pd.to_numeric(df['low']) - pd.to_numeric(df['close']).shift())  # low - previous close
    df['TR']=df[['H-L','H-PC','L-PC']].max(axis=1)
    df['ATR']=np.nan
    df.ix[n-1,'ATR']=df['TR'][:n-1].mean() #.ix is deprecated from pandas version- 0.19
    for i in range(n,len(df)):
        df['ATR'][i]=(df['ATR'][i-1]*(n-1)+ df['TR'][i])/n
    return

StockList=['ITC', 'TCS']

for stock in StockList:
    data[stock] = breeze.get_historical_data(interval="1minute",
                                       from_date="2022-9-2T07:00:00.000Z",
                                       to_date="2022-9-2T18:00:00.000Z",
                                       stock_code=stock,
                                       exchange_code="NSE",
                                       product_type="others")

# for stock in data:
#     if data[stock].empty:
#         print(stock)

# for stock in data:
#     print(stock, data[stock].head())

#
# for stock in data:
#     data[stock].drop(data[stock][data[stock].Volume == 0].index, inplace=True) # Data Cleaning
#     ATR(data[stock],n)
#     data[stock]=data[stock][['Open','High','Low','Close','ATR']] # Removing unwanted columns



for stock in data:
    renkoData[stock]={'BrickSize':0.0, 'Open':0.0,'Close':0.0,'Color':''}

for stock in data:
    renkoData[stock]['BrickSize']=round(data[stock]['ATR'][-1],2) #This can be set manually as well!
    renkoData[stock]['Open']=renkoData[stock]['BrickSize']+renkoData[stock]['Close'] # This can be done the otherway round as well.'Close' = 'BrickSize' - 'Open'
    renkoData[stock]['Color']='red'    # Should you choose to do the other way round, please change the color to 'green'

for stock in data:
    finalData[stock]=pd.DataFrame()
    finalData[stock].index.name='Date'
    finalData[stock]['ReOpen']=0.0
    finalData[stock]['ReHigh']=0.0
    finalData[stock]['ReLow']=0.0
    finalData[stock]['ReClose']=0.0
    finalData[stock]['Color']=''

for stock in data:  # This loops thorugh all the stocks in the data dictionary
    for index, row in data[
        stock].iterrows():  # One may choose to use Pure python instead of Iterrows to loop though each n
        # every row to improve performace if datasets are large.
        if renkoData[stock]['Open'] > renkoData[stock]['Close']:
            while row['Close'] > renkoData[stock]['Open'] + renkoData[stock]['BrickSize']:
                renkoData[stock]['Open'] += renkoData[stock]['BrickSize']
                renkoData[stock]['Close'] += renkoData[stock]['BrickSize']
                finalData[stock].loc[index] = row
                finalData[stock]['ReOpen'].loc[index] = renkoData[stock]['Close']
                finalData[stock]['ReHigh'].loc[index] = renkoData[stock]['Open']
                finalData[stock]['ReLow'].loc[index] = renkoData[stock]['Close']
                finalData[stock]['ReClose'].loc[index] = renkoData[stock]['Open']
                finalData[stock]['Color'].loc[index] = 'green'

            while row['Close'] < renkoData[stock]['Close'] - renkoData[stock]['BrickSize']:
                renkoData[stock]['Open'] -= renkoData[stock]['BrickSize']
                renkoData[stock]['Close'] -= renkoData[stock]['BrickSize']
                finalData[stock].loc[index] = row
                finalData[stock]['ReOpen'].loc[index] = renkoData[stock]['Open']
                finalData[stock]['ReHigh'].loc[index] = renkoData[stock]['Open']
                finalData[stock]['ReLow'].loc[index] = renkoData[stock]['Close']
                finalData[stock]['ReClose'].loc[index] = renkoData[stock]['Close']
                finalData[stock]['Color'].loc[index] = 'red'

        else:
            while row['Close'] < renkoData[stock]['Open'] - renkoData[stock]['BrickSize']:
                renkoData[stock]['Open'] -= renkoData[stock]['BrickSize']
                renkoData[stock]['Close'] -= renkoData[stock]['BrickSize']
                finalData[stock].loc[index] = row
                finalData[stock]['ReOpen'].loc[index] = renkoData[stock]['Close']
                finalData[stock]['ReHigh'].loc[index] = renkoData[stock]['Close']
                finalData[stock]['ReLow'].loc[index] = renkoData[stock]['Open']
                finalData[stock]['ReClose'].loc[index] = renkoData[stock]['Open']
                finalData[stock]['Color'].loc[index] = 'red'

            while row['Close'] > renkoData[stock]['Close'] + renkoData[stock]['BrickSize']:
                renkoData[stock]['Open'] += renkoData[stock]['BrickSize']
                renkoData[stock]['Close'] += renkoData[stock]['BrickSize']
                finalData[stock].loc[index] = row
                finalData[stock]['ReOpen'].loc[index] = renkoData[stock]['Open']
                finalData[stock]['ReHigh'].loc[index] = renkoData[stock]['Close']
                finalData[stock]['ReLow'].loc[index] = renkoData[stock]['Open']
                finalData[stock]['ReClose'].loc[index] = renkoData[stock]['Close']
                finalData[stock]['Color'].loc[index] = 'green'