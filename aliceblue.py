from datetime import datetime
from datetime import timedelta
from alice_blue import *
from pya3 import *
from datetime import datetime, date, time, timedelta

alice = Aliceblue(user_id='AB133347',api_key='vjXB0KDZ0fiOSOISnyY0x6ZJI3TTV0uKQbnqL3N8lTHAzyCZohZV3ohjAduLTjMP8ELfhy6ibvQX82S0vLoKGDN3iAzNJtzZSQ6s')

print(alice.get_session_id()) # Get Session ID

# instrument = alice.get_instrument_by_symbol("NFO", "RELIANCE")
# from_datetime = datetime.now() - datetime.timedelta(days=7)     # From last & days
# to_datetime = datetime.now()                                    # To now
# interval = "15"       # ["1", "2", "3", "4", "5", "10", "15", "30", "60", "120", "180", "240", "D", "1W", "1M"]
# indices = False      # For Getting index data
# # print(alice.get_historical(instrument, from_datetime, to_datetime, interval, indices))
print(alice.get_historical(alice.get_instrument_by_symbol("NFO", "ITC"), datetime(2022,8,26), datetime(2022,8,26), "5", False))


