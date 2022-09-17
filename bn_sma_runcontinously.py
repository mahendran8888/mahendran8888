import datetime
import time
import smacorrection
from breeze_connect import BreezeConnect
import numpy as np
Login details here

now = datetime.datetime.now()

minute = now.minute

while minute <= 59 :
    smacorrection.smatest()
    print(datetime.datetime.now())
    time.sleep(60)
    minute = now.minute
