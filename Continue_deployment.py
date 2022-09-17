import datetime
import time
import deployment0001
from breeze_connect import BreezeConnect
import numpy as np

Login details here

now = datetime.datetime.now()

minute = now.minute

while minute <= 59 :
    deployment0001.smatest()
    print(datetime.datetime.now())
    time.sleep(60)
    minute = now.minute
