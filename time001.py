import time

# get current local time
t = time.localtime(time.time())

if t.tm_sec == 0:
	print("Y")
else:
	print("N")