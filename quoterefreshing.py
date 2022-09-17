import datetime
import time
import breezequote01
now = datetime.datetime.now()

minute = now.minute

while minute <= 59 :
    breezequote01.qt()
    print(datetime.datetime.now())
    time.sleep(1)
    minute = now.minute