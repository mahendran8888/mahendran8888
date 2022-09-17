import datetime
import time
import breezequotetest
now = datetime.datetime.now()

minute = now.minute

while minute <= 59 :
    breezequotetest.qt()
    print(datetime.datetime.now())
    time.sleep(1)
    minute = now.minute