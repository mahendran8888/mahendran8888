from datetime import datetime, date, time, timedelta
from alice_blue import *

access_token = AliceBlue.login_and_get_access_token(username='AB133347', password='pragati@3', twoFA='1985', api_secret='vjXB0KDZ0fiOSOISnyY0x6ZJI3TTV0uKQbnqL3N8lTHAzyCZohZV3ohjAduLTjMP8ELfhy6ibvQX82S0vLoKGDN3iAzNJtzZSQ6s',
                                                    app_id='jvbqTE5sF8')
alice = AliceBlue(username='AB133347', password='pragati@3', access_token=access_token)

instrument = alice.get_instrument_by_symbol("NFO", "RELIANCE")
from_datetime = datetime.now() - datetime.timedelta(days=7)     # From last & days
to_datetime = datetime.now()                                    # To now
interval = "15"       # ["1", "2", "3", "4", "5", "10", "15", "30", "60", "120", "180", "240", "D", "1W", "1M"]
indices = False      # For Getting index data
print(alice.get_historical(instrument, from_datetime, to_datetime, interval, indices))
