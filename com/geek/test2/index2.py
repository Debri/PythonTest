def my_sum(*arg):
    if len(arg) == 0:
        return 0
    for val in arg:
        if not isinstance(val, int):
            return 0
    return sum(arg)


def my_average(*arg):
    if len(arg) == 0:
        return 0
    for val in arg:
        if not isinstance(val, int):
            return 0

    return sum(arg) / len(arg)


# 使用闭包
def dec(func):
    def in_dec(*arg):
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val, int):
                return 0
        return func(*arg)

    return in_dec


my = dec(my_sum)
print(my(1, 2, 3))

j = dec(my_average(1, 2, 3))
print(j)
# 神奇！！！！
# print(my_sum(1, 2, 34, '3'))
# print(my_sum(1, 2, 3, 4))
