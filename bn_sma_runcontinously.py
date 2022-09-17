import datetime
import time
import smacorrection
from breeze_connect import BreezeConnect
import numpy as np

breeze = BreezeConnect(api_key="1kA440t7401177L329z1I79H5R0J49y1")
breeze.generate_session(api_secret="~2211636ES2RD9462951909401o+e597", session_token="1536299")

now = datetime.datetime.now()

minute = now.minute

while minute <= 59 :
    smacorrection.smatest()
    print(datetime.datetime.now())
    time.sleep(60)
    minute = now.minute