import datetime
now = datetime.datetime.now()

print(now)

then = datetime.datetime(2016, 9, 13, 11, 0, 0)

delta = now - then

print(delta.days, 'days ago')

print(then.strftime("%Y-%m-%d"))

after = now + datetime.timedelta(days=2)
after += datetime.timedelta(seconds=86400)

print(after.strftime("%Y-%m-%d"))

import time

lst = []
for i in range(5):
    lst.append(datetime.datetime.now())
    time.sleep(2)

print(lst)
