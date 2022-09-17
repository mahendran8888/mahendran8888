from breeze_connect import BreezeConnect
import pandas as pd
import xlwings as xw
import datetime
breeze = BreezeConnect(api_key="6C9kU52s67r789$507424(0f6t32515l")
breeze.generate_session(api_secret="9s362t4G99+j37q929&20800~857Es+9", session_token="1576356")

# df = pd.read_csv("C:\\Users\\mahen\\OneDrive\\Documents\\SecurityMaster\\NSEScripMaster.csv", low_memory=False)
# stockcode = df['ShortName'].tolist()
# print(stockcode)
# for i in symbol:
# stockcode = ['BPL','ACC','BEML','ITC','ABB','TCS']
df = pd.read_csv("C:\\Users\\mahen\\OneDrive\\Documents\\fno.csv", low_memory=False)
stockcode = df['stockcode'].tolist()
print(stockcode)
appended_data = []
for i in stockcode:
    # print(i)
    data1 = breeze.get_quotes(stock_code=i,
                exchange_code="NSE",
                expiry_date="2022-08-04T06:00:00.000Z",
                product_type="cash",
                right="others",
                strike_price="0")
    # print(data1)
    df = pd.DataFrame(data1["Success"])
    df1 = df.loc[df['exchange_code'] == 'NSE']
    # df1 = pd.DataFrame(df)
    appended_data.append(df1)
appended_data = pd.concat(appended_data)
print(appended_data)
# wb = xw.Book('C:\\Users\\mahen\\OneDrive\\Desktop\\Test.xlsx')
# # wb.api.RefreshAll()
# sht1 = wb.sheets['Sheet1']
# xw.Range('A1').value = df = appended_data
# xw.Range('A1').options(pd.DataFrame, expand='table').value


# Futures
# {'Success': [{'exchange_code': 'NFO', 'product_type': 'Future', 'stock_code': 'ITC', 'expiry_date': '25-Aug-2022', 'right': '*', 'strike_price': 0.0, 'ltp': 310.3, 'ltt': '04-Aug-2022 10:30:13', 'best_bid_price': 310.2, 'best_bid_quantity': '6400', 'best_offer_price': 310.35, 'best_offer_quantity': '6400', 'open': 309.15, 'high': 311.0, 'low': 308.8, 'previous_close': 309.3, 'ltp_percent_change': 32.0, 'upper_circuit': 340.25, 'lower_circuit': 278.4, 'total_quantity_traded': '5328000', 'spot_price': '309.65'}], 'Status': 200, 'Error': None}

# cash
# {'Success': [{'exchange_code': 'NSE', 'product_type': '', 'stock_code': 'ITC', 'expiry_date': None, 'right': None, 'strike_price': 0.0, 'ltp': 309.65, 'ltt': '04-Aug-2022 10:31:29', 'best_bid_price': 309.65, 'best_bid_quantity': '449', 'best_offer_price': 309.7, 'best_offer_quantity': '5619', 'open': 308.0, 'high': 310.25, 'low': 307.25, 'previous_close': 308.15, 'ltp_percent_change': 0.486775920817784, 'upper_circuit': 338.95, 'lower_circuit': 277.35, 'total_quantity_traded': '3756671', 'spot_price': None}, {'exchange_code': 'BSE', 'product_type': '', 'stock_code': 'ITC', 'expiry_date': None, 'right': None, 'strike_price': 0.0, 'ltp': 309.5, 'ltt': '04-Aug-2022 10:31:30', 'best_bid_price': 309.65, 'best_bid_quantity': '100', 'best_offer_price': 309.7, 'best_offer_quantity': '455', 'open': 310.0, 'high': 310.35, 'low': 307.35, 'previous_close': 308.1, 'ltp_percent_change': 0.454397922752353, 'upper_circuit': 338.9, 'lower_circuit': 277.3, 'total_quantity_traded': '172307', 'spot_price': None}], 'Status': 200, 'Error': None}

