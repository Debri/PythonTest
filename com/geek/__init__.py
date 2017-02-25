import time

import datetime


def funcyion(str):
    print(str)
    return


print("hello world")
if True:
    print("true")
else:
    print("false")
print("123")
print(1)
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(tinydict['code'])

i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): print(i), " 是素数"
    i = i + 1
er = "hello"
print(er[1:2])
print(time.time())
print(time.localtime(time.time()))
