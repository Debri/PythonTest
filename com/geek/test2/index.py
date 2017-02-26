passline = 60


# 闭包和作用域的问题
def func():
    passline = 100
    print(passline)


def func1():
    print(passline)


func()
func1()
