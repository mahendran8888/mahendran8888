import datetime
import time
import deployment0001
from breeze_connect import BreezeConnect
import numpy as np

breeze = BreezeConnect(api_key="w388658u78t85712+T22!484t0092*81")
breeze.generate_session(api_secret="y56&ZBD2n=3219002f`78PyZI888H251", session_token="1488474")

now = datetime.datetime.now()

minute = now.minute

while minute <= 59 :
    deployment0001.smatest()
    print(datetime.datetime.now())
    time.sleep(60)
    minute = now.minute