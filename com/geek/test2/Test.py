import time


# 高阶函数，作用相当于java中的代理
# 使用原理是函数可以赋值到一个变量，然后将这个变量作为参数传递到另一个函数中，实现了函数作为参数传递到方法中

def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print('call %s() in %fs' % (f.__name__, (t2 - t1)))
        return r

    return fn


@performance
def factorial(n):
    from functools import reduce
    return reduce(lambda x, y: x * y, range(1, n + 1))


print
factorial(10)
