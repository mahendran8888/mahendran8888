# import logging
import datetime
import statistics
from time import sleep
from alice_blue import *

# Config
access_token = AliceBlue.login_and_get_access_token(username='AB133347', password='pragati@3', twoFA='1985',
                                                    api_secret='bb4azbDnhxfJ7bbTKfd4gWjN8yc3IOXLykCLOfqvrdU3ixAONzyqe6dT0qh4xaeZ',
                                                    app_id='jvbqTE5sF8')
alice = AliceBlue(username='AB133347', password='pragati@3', access_token=access_token)
EMA_CROSS_SCRIP = 'INFY'
# logging.basicConfig(level=logging.DEBUG)  # Optional for getting debug messages.
# Config

ltp = 0
high = 0
low = 0
socket_opened = False
alice = None


def event_handler_quote_update(message):
    global ltp, high, low
    ltp = message['ltp']
    high = message['high']
    low = message['low']
    phigh = message['high'][-1]
    plow = message['low'][-1]



def open_callback():
    global socket_opened
    socket_opened = True


def buy_signal(ins_scrip):
    global alice
    alice.place_order(transaction_type=TransactionType.Buy,
                      instrument=ins_scrip,
                      quantity=1,
                      order_type=OrderType.Market,
                      product_type=ProductType.Intraday,
                      price=0.0,
                      trigger_price=None,
                      stop_loss=None,
                      square_off=None,
                      trailing_sl=None,
                      is_amo=False)


def sell_signal(ins_scrip):
    global alice
    alice.place_order(transaction_type=TransactionType.Sell,
                      instrument=ins_scrip,
                      quantity=1,
                      order_type=OrderType.Market,
                      product_type=ProductType.Intraday,
                      price=0.0,
                      trigger_price=None,
                      stop_loss=None,
                      square_off=None,
                      trailing_sl=None,
                      is_amo=False)


def main():
    global socket_opened
    global alice
    # global username
    # global password
    # global twoFA
    # global api_secret
    global EMA_CROSS_SCRIP
    minute_close = []
    access_token = AliceBlue.login_and_get_access_token(username='AB133347', password='pragati@3', twoFA='1985',
                                                        api_secret='bb4azbDnhxfJ7bbTKfd4gWjN8yc3IOXLykCLOfqvrdU3ixAONzyqe6dT0qh4xaeZ',
                                                        app_id='jvbqTE5sF8')
    alice = AliceBlue(username='AB133347', password='pragati@3', access_token=access_token)

    ins_scrip = alice.get_instrument_by_symbol('NSE', EMA_CROSS_SCRIP)

    socket_opened = False
    alice.start_websocket(subscribe_callback=event_handler_quote_update,
                          socket_open_callback=open_callback,
                          run_in_background=True)

    while (socket_opened == False):  # wait till socket open & then subscribe
        pass
    alice.subscribe(ins_scrip, LiveFeedType.COMPACT)

    current_signal = ''
    while True:
        if (datetime.datetime.now().second == 0):
            minute_close.append(ltp)
            if (len(minute_close) > 10):
                # sma_5 = statistics.mean(minute_close[-5:])
                sma_10 = statistics.mean(minute_close[-10:])
                print(sma_10)
                psma_10 = sma_10[-1]
                print(sma_10[-1])

                if (current_signal != 'buy'):
                    if (low > sma_10 and plow < psma_10 ):
                        buy_signal(ins_scrip)
                        current_signal = 'buy'
                if (current_signal != 'sell'):
                    if (high < sma_10 and high > sma_10):
                        sell_signal(ins_scrip)
                        current_signal = 'sell'
            sleep(1)
        sleep(0.2)  # sleep for 200ms


if (__name__ == '__main__'):
    main()