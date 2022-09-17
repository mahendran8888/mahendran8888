from breeze_connect import BreezeConnect

breeze = BreezeConnect(api_key="F1o2v998H#L444898z5e6ytB492480a&")
breeze.generate_session(api_secret="J72878G2240318h0p161C49t5Z429T07", session_token="1643844")

# # Place an order from your account.
print(breeze.place_order(stock_code="TATSTE",
                    exchange_code="NSE",
                    product="margin",
                    action="sell",
                    order_type="market",
                    stoploss="0",
                    quantity="1",
                    price="",
                    validity="day",
                    validity_date="",
                    disclosed_quantity="0",
                    expiry_date="",
                    right="others",
                    strike_price="0",
                    user_remark="Executed"))


# Sqauare off an order
# print(breeze.square_off(exchange_code="NSE",
#                     product="margin",
#                     stock_code="TATSTE",
#                     quantity="1",
#                     price="107",
#                     action="buy",
#                     order_type="limit",
#                     validity="day",
#                     stoploss="110",
#                     disclosed_quantity="0",
#                     protection_percentage="",
#                     settlement_id="2022172",
#                     cover_quantity="",
#                     open_quantity="",
#                     margin_amount=""))

# Place target order from your account.
print(breeze.place_order(stock_code="TATSTE",
                    exchange_code="NSE",
                    product="margin",
                    action="buy",
                    order_type="limit",
                    stoploss="0",
                    quantity="1",
                    price="108",
                    validity="day",
                    validity_date="",
                    disclosed_quantity="0",
                    expiry_date="",
                    right="others",
                    strike_price="0",
                    user_remark="Executed"))
#
# # Place stop lose order from your account.
# print(breeze.place_order(stock_code="TATSTE",
#                     exchange_code="NSE",
#                     product="margin",
#                     action="sell",
#                     order_type="limit",
#                     stoploss="0",
#                     quantity="1",
#                     price="107",
#                     validity="day",
#                     validity_date="",
#                     disclosed_quantity="0",
#                     expiry_date="",
#                     right="others",
#                     strike_price="0",
#                     user_remark="Executed"))

# print(Get trade detail of your account.
# breeze.get_trade_detail(exchange_code="NSE",
#                         order_id="20220810N400013470"))
# Get trade list of your account.
# print(breeze.get_trade_list(from_date="2021-01-1T06:00:00.000Z",
#                         to_date="2022-09-07T18:00:00.000Z",
#                         exchange_code="NSE",
#                         product_type="",
#                         action="",
#                         stock_code=""))

# {'Success': [{'book_type': 'Trade-Book', 'trade_date': '17-Aug-2022', 'stock_code': 'ITC', 'action': 'B', 'quantity': '1', 'average_cost': '312.45', 'brokerage_amount': '0.00', 'product_type': 'C', 'exchange_code': 'NSE', 'order_id': '20220817N200043704', 'segment': 'N', 'settlement_code': '2022155', 'dp_id': 'IN303028', 'client_id': '63319957', 'ltp': '312.60', 'eatm_withheld_amount': '0.00', 'cash_withheld_amount': '0.00', 'total_taxes': '0.00', 'order_type': '77', 'expiry_date': None, 'right': None, 'strike_price': None}], 'Status': 200, 'Error': None}


# {'Success': {'order_id': 'Equity CASH Order placed successfully through RI reference no 20220823N200014086', 'message': None}, 'Status': 200, 'Error': None}

# Sqauare off an order
# print(breeze.square_off(source_flag="",
#                     stock_code="TATSTE",
#                     exchange_code="NSE",
#                     quantity="1",
#                     price="108",
#                     action="sell",
#                     order_type="limit",
#                     validity="day",
#                     stoploss="105",
#                     disclosed_quantity="0",
#                     protection_percentage="",
#                     settlement_id="",
#                     margin_amount="",
#                     open_quantity="",
#                     cover_quantity="",
#                     product="margin",
#                     expiry_date="",
#                     right="",
#                     strike_price="",
#                     # trade_date="",
#                     trade_password="",
#                     alias_name=""))

# {'Success': [{'book_type': 'Trade-Book', 'trade_date': '17-Aug-2022', 'stock_code': 'ITC', 'action': 'B', 'quantity': '1', 'average_cost': '312.45', 'brokerage_amount': '0.00', 'product_type': 'C', 'exchange_code': 'NSE', 'order_id': '20220817N200043704', 'segment': 'N', 'settlement_code': '2022155', 'dp_id': 'IN303028', 'client_id': '63319957', 'ltp': '312.50', 'eatm_withheld_amount': '0.00', 'cash_withheld_amount': '0.00', 'total_taxes': '0.00', 'order_type': '77', 'expiry_date': None, 'right': None, 'strike_price': None}], 'Status': 200, 'Error': None}

# {'Success': {'order_id': '20220907N200026313', 'message': 'Equity MARGIN Order placed successfully through RI reference no 20220907N200026313'}, 'Status': 200, 'Error': None}
