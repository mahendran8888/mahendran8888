from breeze_connect import BreezeConnect
import numpy as np
import pandas as pd
from datetime import datetime,date,time,timedelta
from nsepy import get_history
import pandas as pd
import numpy as np
import pandas_ta as ta

# login
breeze = BreezeConnect(api_key="6C9kU52s67r789$507424(0f6t32515l")
breeze.generate_session(api_secret="9s362t4G99+j37q929&20800~857Es+9", session_token="1576356")

# Banknifty direction
bndir = breeze.get_historical_data(interval="1minute", from_date="2022-08-08T07:00:00.000Z", to_date="2022-08-08T18:00:00.000Z", stock_code="CNXBAN", exchange_code="NSE", product_type="cash")
df3 = pd.DataFrame(bndir['Success'])
df3['sma_20'] = df3['ltp'].rolling(20).mean()
if df3['low'] > df3['sma_20']:
    print("Buy")
if df3['low'] < df3['sma_20']:
    print("Sell")
def buy():
    # get strike price at the money
    bn=breeze.get_quotes(stock_code="CNXBAN",
                        exchange_code="NSE",
                        expiry_date="2022-08-05T06:00:00.000Z",
                        product_type="cash",
                        right="others",
                        strike_price="0")
    df = pd.DataFrame(bn['Success'])
    actual_ltp =df[df['exchange_code'] == 'NSE']['ltp']

    # round premium ltp for strikeproce
    rounded_ltp=round(actual_ltp, -2).to_string(index=False)
    rounded_ltp=pd.to_numeric(rounded_ltp).astype(int)

    # get strike price having premium Rs.100
    for i in range(rounded_ltp + 500, rounded_ltp + 1000, 100):
        bnc = breeze.get_quotes(stock_code="CNXBAN",
                          exchange_code="NFO",
                          expiry_date="2022-08-11T06:00:00.000Z",
                          product_type="options",
                          right="call",
                          strike_price=i)
        df = pd.DataFrame(bnc)
        df1.append(df)
    df1 = pd.concat(df1)
    df1['sq.ltp']=(df1['ltp'] - 100)*(df1['ltp'] - 100)
    # print(bnc)
    df1[df1['sq.ltp'] == df1['sq.ltp'].min(),'strike_price']
    print(df1)

# for j in range(rounded_ltp, rounded_ltp - 1000, -100):
#     bnp = breeze.get_quotes(stock_code="CNXBAN",
#                     exchange_code="NFO",
#                     expiry_date="2022-08-11T06:00:00.000Z",
#                     product_type="options",
#                     right="put",
#                     strike_price=j)
#     df = pd.DataFrame(bnp)
#     df1.append(df)
# df1 = pd.concat(df1)
# # print(bnp)





#
# {'Success': [{'exchange_code': 'NFO', 'product_type': '', 'stock_code': 'CNXBAN', 'expiry_date': '11-Aug-2022', 'right': 'C', 'strike_price': 39300.0, 'ltp': 32.2, 'ltt': '05-Aug-2022 12:10:28', 'best_bid_price': 32.0, 'best_bid_quantity': '1225', 'best_offer_price': 32.15, 'best_offer_quantity': '700', 'open': 35.0, 'high': 45.7, 'low': 28.85, 'previous_close': 34.15, 'ltp_percent_change': -571.0, 'upper_circuit': 628.5, 'lower_circuit': 0.05, 'total_quantity_traded': '3291550', 'spot_price': '38094.1'}], 'Status': 200, 'Error': None}
# {'Success': [{'exchange_code': 'NFO', 'product_type': '', 'stock_code': 'CNXBAN', 'expiry_date': '11-Aug-2022', 'right': 'C', 'strike_price': 39400.0, 'ltp': 25.9, 'ltt': '05-Aug-2022 12:10:30', 'best_bid_price': 25.85, 'best_bid_quantity': '800', 'best_offer_price': 25.95, 'best_offer_quantity': '325', 'open': 32.95, 'high': 37.8, 'low': 24.4, 'previous_close': 28.9, 'ltp_percent_change': -1038.0, 'upper_circuit': 574.95, 'lower_circuit': 0.05, 'total_quantity_traded': '3373125', 'spot_price': '38094.1'}], 'Status': 200, 'Error': None}
# {'Success': [{'exchange_code': 'NFO', 'product_type': '', 'stock_code': 'CNXBAN', 'expiry_date': '11-Aug-2022', 'right': 'C', 'strike_price': 39500.0, 'ltp': 21.3, 'ltt': '05-Aug-2022 12:10:32', 'best_bid_price': 21.35, 'best_bid_quantity': '125', 'best_offer_price': 21.45, 'best_offer_quantity': '1800', 'open': 21.3, 'high': 31.55, 'low': 20.25, 'previous_close': 24.9, 'ltp_percent_change': -1446.0, 'upper_circuit': 525.2, 'lower_circuit': 0.05, 'total_quantity_traded': '8844775', 'spot_price': '38095.9'}], 'Status': 200, 'Error': None}
# {'Success': [{'exchange_code': 'NFO', 'product_type': '', 'stock_code': 'CNXBAN', 'expiry_date': '11-Aug-2022', 'right': 'P', 'strike_price': 38100.0, 'ltp': 376.9, 'ltt': '05-Aug-2022 12:10:31', 'best_bid_price': 376.6, 'best_bid_quantity': '25', 'best_offer_price': 377.0, 'best_offer_quantity': '1150', 'open': 579.9, 'high': 607.0, 'low': 352.9, 'previous_close': 631.2, 'ltp_percent_change': -4029.0, 'upper_circuit': 1952.35, 'lower_circuit': 0.05, 'total_quantity_traded': '8698425', 'spot_price': '38095.9'}], 'Status': 200, 'Error': None}
# {'Success': [{'exchange_code': 'NFO', 'product_type': '', 'stock_code': 'CNXBAN', 'expiry_date': '11-Aug-2022', 'right': 'P', 'strike_price': 38000.0, 'ltp': 331.4, 'ltt': '05-Aug-2022 12:10:32', 'best_bid_price': 330.85, 'best_bid_quantity': '25', 'best_offer_price': 331.4, 'best_offer_quantity': '25', 'open': 531.2, 'high': 549.25, 'low': 308.75, 'previous_close': 572.1, 'ltp_percent_change': -4207.0, 'upper_circuit': 1834.05, 'lower_circuit': 0.05, 'total_quantity_traded': '30690650', 'spot_price': '38095.9'}], 'Status': 200, 'Error': None}
# {'Success': [{'exchange_code': 'NFO', 'product_type': '', 'stock_code': 'CNXBAN', 'expiry_date': '11-Aug-2022', 'right': 'P', 'strike_price': 37900.0, 'ltp': 292.55, 'ltt': '05-Aug-2022 12:10:33', 'best_bid_price': 292.35, 'best_bid_quantity': '150', 'best_offer_price': 292.8, 'best_offer_quantity': '50', 'open': 459.4, 'high': 493.95, 'low': 271.65, 'previous_close': 513.55, 'ltp_percent_change': -4303.0, 'upper_circuit': 1715.8, 'lower_circuit': 0.05, 'total_quantity_traded': '16923650', 'spot_price': '38089.85'}], 'Status': 200, 'Error': None}
# {'Success': [{'exchange_code': 'NFO', 'product_type': '', 'stock_code': 'CNXBAN', 'expiry_date': '11-Aug-2022', 'right': 'P', 'strike_price': 37800.0, 'ltp': 255.5, 'ltt': '05-Aug-2022 12:10:33', 'best_bid_price': 255.2, 'best_bid_quantity': '375', 'best_offer_price': 255.7, 'best_offer_quantity': '75', 'open': 462.95, 'high': 462.95, 'low': 237.0, 'previous_close': 459.1, 'ltp_percent_change': -4435.0, 'upper_circuit': 1601.2, 'lower_circuit': 0.05, 'total_quantity_traded': '20916350', 'spot_price': '38090.5'}], 'Status': 200, 'Error': None}
# {'Success': [{'exchange_code': 'NFO', 'product_type': '', 'stock_code': 'CNXBAN', 'expiry_date': '11-Aug-2022', 'right': 'P', 'strike_price': 37700.0, 'ltp': 223.0, 'ltt': '05-Aug-2022 12:10:33', 'best_bid_price': 222.8, 'best_bid_quantity': '25', 'best_offer_price': 223.0, 'best_offer_quantity': '1000', 'open': 410.0, 'high': 410.0, 'low': 205.55, 'previous_close': 415.6, 'ltp_percent_change': -4634.0, 'upper_circuit': 1497.55, 'lower_circuit': 0.05, 'total_quantity_traded': '13402675', 'spot_price': '38090.5'}], 'Status': 200, 'Error': None}
# {'Success': [{'exchange_code': 'NFO', 'product_type': '', 'stock_code': 'CNXBAN', 'expiry_date': '11-Aug-2022', 'right': 'P', 'strike_price': 37600.0, 'ltp': 193.8, 'ltt': '05-Aug-2022 12:10:34', 'best_bid_price': 193.8, 'best_bid_quantity': '25', 'best_offer_price': 194.2, 'best_offer_quantity': '25', 'open': 374.6, 'high': 374.65, 'low': 178.2, 'previous_close': 368.3, 'ltp_percent_change': -4738.0, 'upper_circuit': 1390.05, 'lower_circuit': 0.05, 'total_quantity_traded': '9551275', 'spot_price': '38090.5'}], 'Status': 200, 'Error': None}
# {'Success': [{'exchange_code': 'NFO', 'product_type': '', 'stock_code': 'CNXBAN', 'expiry_date': '11-Aug-2022', 'right': 'P', 'strike_price': 37500.0, 'ltp': 168.05, 'ltt': '05-Aug-2022 12:10:35', 'best_bid_price': 167.6, 'best_bid_quantity': '450', 'best_offer_price': 168.0, 'best_offer_quantity': '75', 'open': 299.0, 'high': 311.3, 'low': 153.75, 'previous_close': 325.05, 'ltp_percent_change': -4830.0, 'upper_circuit': 1287.1, 'lower_circuit': 0.05, 'total_quantity_traded': '20505900', 'spot_price': '38093.45'}], 'Status': 200, 'Error': None}
# {'Success': [{'exchange_code': 'NFO', 'product_type': '', 'stock_code': 'CNXBAN', 'expiry_date': '11-Aug-2022', 'right': 'P', 'strike_price': 37400.0, 'ltp': 145.6, 'ltt': '05-Aug-2022 12:10:33', 'best_bid_price': 145.5, 'best_bid_quantity': '175', 'best_offer_price': 145.9, 'best_offer_quantity': '700', 'open': 289.65, 'high': 289.65, 'low': 133.4, 'previous_close': 288.65, 'ltp_percent_change': -4956.0, 'upper_circuit': 1191.95, 'lower_circuit': 0.05, 'total_quantity_traded': '6685175', 'spot_price': '38093.45'}], 'Status': 200, 'Error': None}
# {'Success': [{'exchange_code': 'NFO', 'product_type': '', 'stock_code': 'CNXBAN', 'expiry_date': '11-Aug-2022', 'right': 'P', 'strike_price': 37300.0, 'ltp': 124.8, 'ltt': '05-Aug-2022 12:10:31', 'best_bid_price': 125.55, 'best_bid_quantity': '150', 'best_offer_price': 125.85, 'best_offer_quantity': '475', 'open': 248.65, 'high': 248.65, 'low': 115.05, 'previous_close': 250.85, 'ltp_percent_change': -5025.0, 'upper_circuit': 1095.85, 'lower_circuit': 0.05, 'total_quantity_traded': '6915000', 'spot_price': '38092.5'}], 'Status': 200, 'Error': None}
# {'Success': [{'exchange_code': 'NFO', 'product_type': '', 'stock_code': 'CNXBAN', 'expiry_date': '11-Aug-2022', 'right': 'P', 'strike_price': 37200.0, 'ltp': 109.0, 'ltt': '05-Aug-2022 12:10:35', 'best_bid_price': 108.4, 'best_bid_quantity': '275', 'best_offer_price': 108.75, 'best_offer_quantity': '175', 'open': 218.65, 'high': 218.65, 'low': 99.1, 'previous_close': 219.95, 'ltp_percent_change': -5044.0, 'upper_circuit': 1008.25, 'lower_circuit': 0.05, 'total_quantity_traded': '6609525', 'spot_price': '38092.5'}], 'Status': 200, 'Error': None}
# {'Success': [{'exchange_code': 'NFO', 'product_type': '', 'stock_code': 'CNXBAN', 'expiry_date': '11-Aug-2022', 'right': 'P', 'strike_price': 37100.0, 'ltp': 93.4, 'ltt': '05-Aug-2022 12:10:35', 'best_bid_price': 93.0, 'best_bid_quantity': '25', 'best_offer_price': 93.1, 'best_offer_quantity': '25', 'open': 197.65, 'high': 197.65, 'low': 85.6, 'previous_close': 191.45, 'ltp_percent_change': -5121.0, 'upper_circuit': 924.25, 'lower_circuit': 0.05, 'total_quantity_traded': '4348475', 'spot_price': '38092.2'}], 'Status': 200, 'Error': None}
# {'Success': [{'exchange_code': 'NFO', 'product_type': '', 'stock_code': 'CNXBAN', 'expiry_date': '11-Aug-2022', 'right': 'P', 'strike_price': 37000.0, 'ltp': 80.1, 'ltt': '05-Aug-2022 12:10:36', 'best_bid_price': 80.0, 'best_bid_quantity': '500', 'best_offer_price': 80.25, 'best_offer_quantity': '575', 'open': 146.05, 'high': 162.55, 'low': 74.0, 'previous_close': 169.0, 'ltp_percent_change': -5260.0, 'upper_circuit': 847.65, 'lower_circuit': 0.05, 'total_quantity_traded': '17469975', 'spot_price': '38092.2'}], 'Status': 200, 'Error': None}
# {'Success': [{'exchange_code': 'NFO', 'product_type': '', 'stock_code': 'CNXBAN', 'expiry_date': '11-Aug-2022', 'right': 'P', 'strike_price': 36900.0, 'ltp': 69.2, 'ltt': '05-Aug-2022 12:10:37', 'best_bid_price': 69.3, 'best_bid_quantity': '25', 'best_offer_price': 69.45, 'best_offer_quantity': '50', 'open': 146.55, 'high': 146.55, 'low': 63.9, 'previous_close': 148.15, 'ltp_percent_change': -5329.0, 'upper_circuit': 774.75, 'lower_circuit': 0.05, 'total_quantity_traded': '4014500', 'spot_price': '38092.2'}], 'Status': 200, 'Error': None}
# {'Success': [{'exchange_code': 'NFO', 'product_type': '', 'stock_code': 'CNXBAN', 'expiry_date': '11-Aug-2022', 'right': 'P', 'strike_price': 36800.0, 'ltp': 59.9, 'ltt': '05-Aug-2022 12:10:36', 'best_bid_price': 59.75, 'best_bid_quantity': '150', 'best_offer_price': 59.95, 'best_offer_quantity': '150', 'open': 72.0, 'high': 126.25, 'low': 55.2, 'previous_close': 128.95, 'ltp_percent_change': -5355.0, 'upper_circuit': 705.3, 'lower_circuit': 0.05, 'total_quantity_traded': '4827525', 'spot_price': '38092.2'}], 'Status': 200, 'Error': None}
# {'Success': [{'exchange_code': 'NFO', 'product_type': '', 'stock_code': 'CNXBAN', 'expiry_date': '11-Aug-2022', 'right': 'P', 'strike_price': 36700.0, 'ltp': 51.8, 'ltt': '05-Aug-2022 12:10:35', 'best_bid_price': 51.55, 'best_bid_quantity': '300', 'best_offer_price': 51.75, 'best_offer_quantity': '400', 'open': 107.0, 'high': 108.9, 'low': 48.0, 'previous_close': 115.0, 'ltp_percent_change': -5496.0, 'upper_circuit': 643.25, 'lower_circuit': 0.05, 'total_quantity_traded': '3760850', 'spot_price': '38092.85'}], 'Status': 200, 'Error': None}
#
# Process finished with exit code 0