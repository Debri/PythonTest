# from concurrent.futures import thread
#
# thread.start_new_thread()
a, b = 0, 1
while b < 100000:
    print(b, end=',')
    a, b = b, a + b
