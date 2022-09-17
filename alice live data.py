from alice_blue import *
from time import sleep

Login details here

socket_opened = False
def event_handler_quote_update(message):
    print(f"quote update {message}")

def open_callback():
    global socket_opened
    socket_opened = True

alice.start_websocket(subscribe_callback=event_handler_quote_update,
                      socket_open_callback=open_callback,
                      run_in_background=True)
while(socket_opened==False):
    pass
print(alice.subscribe(alice.get_instrument_by_symbol('NSE', 'ONGC'), LiveFeedType.MARKET_DATA))
sleep(10)
