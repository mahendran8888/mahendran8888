from breeze_connect import BreezeConnect

Login details here
print(breeze.get_funds())

# breeze.get_option_chain_quotes(stock_code="CNXBAN",
#                     exchange_code="NFO",
#                     product_type="options",
#                     expiry_date="2022-09-29T06:00:00.000Z",
#                     right="call",
#                     strike_price="39000")

print(breeze.get_portfolio_positions())


# {'Success': [{'segment': 'equity', 'product_type': 'Margin', 'exchange_code': 'NSE', 'stock_code': 'TATSTE', 'expiry_date': None, 'strike_price': None, 'right': None, 'action': 'Sell', 'quantity': '1', 'average_price': '107', 'settlement_id': '2022172', 'margin_amount': '21.4', 'ltp': '107.2', 'price': '0', 'stock_index_indicator': None, 'cover_quantity': '0', 'stoploss_trigger': None, 'stoploss': '0', 'take_profit': '0', 'available_margin': '21.2', 'squareoff_mode': 'S', 'mtf_sell_quantity': '0', 'mtf_net_amount_payable': '85.6', 'mtf_expiry_date': '*', 'order_id': '*', 'cover_order_flow': '*', 'cover_order_executed_quantity': '0', 'pledge_status': 'NA', 'pnl': '-0.2', 'underlying': None}, {'segment': 'equity', 'product_type': 'Cash', 'exchange_code': 'BSE', 'stock_code': 'PCSIND', 'expiry_date': None, 'strike_price': None, 'right': None, 'action': 'Buy', 'quantity': '50', 'average_price': '19.15', 'settlement_id': '2022672', 'margin_amount': '0', 'ltp': '18.8', 'price': '0', 'stock_index_indicator': None, 'cover_quantity': '0', 'stoploss_trigger': None, 'stoploss': '0', 'take_profit': '0', 'available_margin': '0', 'squareoff_mode': '*', 'mtf_sell_quantity': '0', 'mtf_net_amount_payable': '0', 'mtf_expiry_date': '*', 'order_id': '*', 'cover_order_flow': '*', 'cover_order_executed_quantity': '0', 'pledge_status': '', 'pnl': '0', 'underlying': None}, {'segment': 'equity', 'product_type': 'Cash', 'exchange_code': 'BSE', 'stock_code': 'SURTEX', 'expiry_date': None, 'strike_price': None, 'right': None, 'action': 'Buy', 'quantity': '100', 'average_price': '12.18', 'settlement_id': '2022172', 'margin_amount': '0', 'ltp': '12.21', 'price': '0', 'stock_index_indicator': None, 'cover_quantity': '0', 'stoploss_trigger': None, 'stoploss': '0', 'take_profit': '0', 'available_margin': '0', 'squareoff_mode': '*', 'mtf_sell_quantity': '0', 'mtf_net_amount_payable': '0', 'mtf_expiry_date': '*', 'order_id': '*', 'cover_order_flow': '*', 'cover_order_executed_quantity': '0', 'pledge_status': '', 'pnl': '0', 'underlying': None}], 'Status': 200, 'Error': None}
