from breeze_connect import BreezeConnect
import urllib
import pandas as pd
breeze = BreezeConnect(api_key="1W8960859342@I0rg534r7K^~9P92H_0")
print("https://api.icicidirect.com/apiuser/login?api_key="+urllib.parse.quote_plus("1W8960859342@I0rg534r7K^~9P92H_0"))

breeze.generate_session(api_secret="69498407bAQ13a90IJ3^66s35pj626Z4",
                      session_token="1476148")
breeze.ws_connect()
def on_ticks(ticks):
    print("Ticks: {}".format(ticks))
breeze.on_ticks = on_ticks
feed = breeze.subscribe_feeds(stock_token="ITC")
print(feed)
# breeze.subscribe_feeds(exchange_code="NFO", stock_code="CNXBANK", product_type="options", expiry_date="25-Aug-2022", strike_price="38100", right="Put", get_exchange_quotes=True, get_market_depth=False)
# feed = breeze.subscribe_feeds(stock_token="4.1!108094")
# breeze.unsubscribe_feeds(exchange_code="NFO", stock_code="ITC", product_type="options", expiry_date="26-May-2022", strike_price="650", right="Put", get_exchange_quotes=True, get_market_depth=False)
# # breeze.unsubscribe_feeds(stock_token="4.1!108094")
# df = pd.DataFrame(feed)
# Print(df)

# Ticks: {'symbol': '4.1!135452', 'open': 7.3, 'last': 6.5, 'high': 7.35, 'low': 6.45, 'change': -9.72, 'bPrice': 6.45, 'bQty': 12800, 'sPrice': 6.55, 'sQty': 35200, 'ltq': 3200, 'avgPrice': 6.83, 'quotes': 'Quotes Data', 'OI': '', 'CHNGOI': '', 'ttq': 1152000, 'totalBuyQt': 444800, 'totalSellQ': 499200, 'ttv': '78.68L', 'trend': '', 'lowerCktLm': 0.05, 'upperCktLm': 16.95, 'ltt': 'Thu Aug  4 09:58:24 2022', 'close': 7.2, 'exchange': 'NSE Futures & Options'}
