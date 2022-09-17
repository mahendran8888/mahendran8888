from datetime import datetime, date, time, timedelta
from alice_blue import *

Login details here

instrument = alice.get_instrument_by_symbol("NFO", "RELIANCE")
from_datetime = datetime.now() - datetime.timedelta(days=7)     # From last & days
to_datetime = datetime.now()                                    # To now
interval = "15"       # ["1", "2", "3", "4", "5", "10", "15", "30", "60", "120", "180", "240", "D", "1W", "1M"]
indices = False      # For Getting index data
print(alice.get_historical(instrument, from_datetime, to_datetime, interval, indices))
