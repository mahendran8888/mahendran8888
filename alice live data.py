from alice_blue import *
from time import sleep

access_token = AliceBlue.login_and_get_access_token(username='AB133347', password='pragati@3', twoFA='1985', api_secret='bb4azbDnhxfJ7bbTKfd4gWjN8yc3IOXLykCLOfqvrdU3ixAONzyqe6dT0qh4xaeZ', app_id='jvbqTE5sF8')
alice = AliceBlue(username='AB133347', password='pragati@3', access_token=access_token)

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