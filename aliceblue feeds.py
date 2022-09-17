alice.subscribe(alice.get_instrument_by_symbol('NSE', 'ONGC'), LiveFeedType.MARKET_DATA)
quote update {'exchange': 'NSE', 'token': 2475, 'ltp': 135.95, 'ltt': 1660895689, 'ltq': 70, 'volume': 25601765, 'best_bid_price': 135.95, 'best_bid_quantity': 17695, 'best_ask_price': 136.0, 'best_ask_quantity': 21, 'total_buy_quantity': 2052819, 'total_sell_quantity': 4881497, 'atp': 136.78, 'exchange_time_stamp': 1660895689, 'open': 137.5, 'high': 138.5, 'low': 135.2, 'close': 135.55, 'yearly_high': 194.95, 'yearly_low': 108.5, 'instrument': Instrument(exchange='NSE', token=2475, symbol='ONGC', name='OIL AND NATURAL GAS CORP.', expiry=None, lot_size=None)}



alice.subscribe(alice.get_instrument_by_symbol('NSE', 'ONGC'), LiveFeedType.COMPACT)
quote update {'exchange': 'NSE', 'token': 2475, 'ltp': 135.85, 'change': 30, 'exchange_time_stamp': 1660895760, 'volume': 12200, 'instrument': Instrument(exchange='NSE', token=2475, symbol='ONGC', name='OIL AND NATURAL GAS CORP.', expiry=None, lot_size=None)}



alice.subscribe(alice.get_instrument_by_symbol('NSE', 'ONGC'), LiveFeedType.SNAPQUOTE)
quote update {'exchange': 'NSE', 'token': 2475, 'buyers': [11, 42, 39, 67, 50], 'bid_prices': [135.75, 135.7, 135.65, 135.6, 135.55], 'bid_quantities': [6759, 18704, 18509, 38105, 53011], 'sellers': [5, 15, 32, 20, 36], 'ask_prices': [135.8, 135.85, 135.9, 135.95, 136.0], 'ask_quantities': [2856, 4077, 12756, 7905, 26470], 'exchange_time_stamp': 1660895811, 'instrument': Instrument(exchange='NSE', token=2475, symbol='ONGC', name='OIL AND NATURAL GAS CORP.', expiry=None, lot_size=None)}




alice.subscribe(alice.get_instrument_by_symbol('NSE', 'ONGC'), LiveFeedType.FULL_SNAPQUOTE)
quote update {'exchange': 'NSE', 'token': 2475, 'buyers': [19, 18, 55, 36, 64], 'bid_prices': [135.8, 135.75, 135.7, 135.65, 135.6], 'bid_quantities': [8158, 9563, 24955, 16564, 35403], 'sellers': [23, 29, 26, 36, 30], 'ask_prices': [135.85, 135.9, 135.95, 136.0, 136.05], 'ask_quantities': [5991, 10531, 9973, 28089, 21233], 'atp': 136.78, 'open': 137.5, 'high': 138.5, 'low': 135.2, 'close': 135.55, 'total_buy_quantity': 1994996, 'total_sell_quantity': 4926154, 'volume': 25738527, 'instrument': Instrument(exchange='NSE', token=2475, symbol='ONGC', name='OIL AND NATURAL GAS CORP.', expiry=None, lot_size=None)}


{'exchange': 'NSE', 'token': 26009, 'ltp': 39002.9, 'change': 4294901971, 'exchange_time_stamp': 1660896987, 'volume': 0, 'instrument': Instrument(exchange='NSE', token=26009, symbol='Nifty Bank', name='Nifty Bank', expiry=None, lot_size=None)}
{'exchange': 'NSE', 'token': 26009, 'ltp': 39002.7, 'change': 4294901951, 'exchange_time_stamp': 1660896988, 'volume': 0, 'instrument': Instrument(exchange='NSE', token=26009, symbol='Nifty Bank', name='Nifty Bank', expiry=None, lot_size=None)}
{'exchange': 'NSE', 'token': 26009, 'ltp': 39005.05, 'change': 4294902186, 'exchange_time_stamp': 1660896989, 'volume': 0, 'instrument': Instrument(exchange='NSE', token=26009, symbol='Nifty Bank', name='Nifty Bank', expiry=None, lot_size=None)}
{'exchange': 'NSE', 'token': 26009, 'ltp': 39004.95, 'change': 4294902176, 'exchange_time_stamp': 1660896990, 'volume': 0, 'instrument': Instrument(exchange='NSE', token=26009, symbol='Nifty Bank', name='Nifty Bank', expiry=None, lot_size=None)}
{'exchange': 'NSE', 'token': 26009, 'ltp': 39003.45, 'change': 4294902026, 'exchange_time_stamp': 1660896991, 'volume': 0, 'instrument': Instrument(exchange='NSE', token=26009, symbol='Nifty Bank', name='Nifty Bank', expiry=None, lot_size=None)}
{'exchange': 'NSE', 'token': 26009, 'ltp': 39004.65, 'change': 4294902146, 'exchange_time_stamp': 1660896992, 'volume': 0, 'instrument': Instrument(exchange='NSE', token=26009, symbol='Nifty Bank', name='Nifty Bank', expiry=None, lot_size=None)}
{'exchange': 'NSE', 'token': 26009, 'ltp': 39002.3, 'change': 4294901911, 'exchange_time_stamp': 1660896993, 'volume': 0, 'instrument': Instrument(exchange='NSE', token=26009, symbol='Nifty Bank', name='Nifty Bank', expiry=None, lot_size=None)}
{'exchange': 'NSE', 'token': 26009, 'ltp': 39003.85, 'change': 4294902066, 'exchange_time_stamp': 1660896994, 'volume': 0, 'instrument': Instrument(exchange='NSE', token=26009, symbol='Nifty Bank', name='Nifty Bank', expiry=None, lot_size=None)}
{'exchange': 'NSE', 'token': 26009, 'ltp': 39005.6, 'change': 4294902241, 'exchange_time_stamp': 1660896995, 'volume': 0, 'instrument': Instrument(exchange='NSE', token=26009, symbol='Nifty Bank', name='Nifty Bank', expiry=None, lot_size=None)}
{'exchange': 'NSE', 'token': 26009, 'ltp': 39010.45, 'change': 4294902726, 'exchange_time_stamp': 1660896996, 'volume': 0, 'instrument': Instrument(exchange='NSE', token=26009, symbol='Nifty Bank', name='Nifty Bank', expiry=None, lot_size=None)}
{'exchange': 'NSE', 'token': 26009, 'ltp': 39011.75, 'change': 4294902856, 'exchange_time_stamp': 1660896997, 'volume': 0, 'instrument': Instrument(exchange='NSE', token=26009, symbol='Nifty Bank', name='Nifty Bank', expiry=None, lot_size=None)}
