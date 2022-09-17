
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

def main():
    global alice, tickerlist

    access_token = AliceBlue.login_and_get_access_token(username='AB133347', password='pragati@3', twoFA='1985',
                                                        api_secret='bb4azbDnhxfJ7bbTKfd4gWjN8yc3IOXLykCLOfqvrdU3ixAONzyqe6dT0qh4xaeZ',
                                                        app_id='jvbqTE5sF8')
    alice = AliceBlue(username='AB133347', password='pragati@3', access_token=access_token)

if socket_opened == False:
    open_socket_now()

while True:
    tickerlist = sheet.range("A2").expand("down").value
    for i in tickerlist:
        if i != None:
            instrument = alice.get_instrument_by_symbol('NSE', i.upper())
            alice.subscribe(instrument, LiveFeedType.MARKET_DATA)
    orderPlacement(tickerlist)

def gettingData(message):
    sheet = xw.Book("F:/alice/new.xlsx").sheet[0]

    cell_no = 0
    for i in tickerlist:
        if i != None:
            if i.upper() == message["instrument"].symbol:
                cell_no = tickerlist.index(i) + 2

    sheet.range("A1").value = ["Script","Lot_Size","Ltp", "High","Low","Open","Volume","Condition","Order_type","Quanity","Order_status"]

    sheet.range(f"B{Cell_no}").value = message["instrument"].lot_size


