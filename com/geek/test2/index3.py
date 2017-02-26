# 使用闭包
def dec(func):
    print("call dec")
    print(func, '------------')

    def in_dec(*arg):
        print('in_dec')
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val, int):
                return 0
        return func(*arg)

    return in_dec


#  使用语法糖 ，或者叫注解？？？
@dec
def my_sum(*arg):  # my_sum=in_dec
    print('my_sum')

    return sum(arg)


def my_average(*arg):
    return sum(arg) / len(arg)


print(my_sum(1, 2, 3))

# my = dec(my_sum)
# print(my(1, 2, 3))
#
# j = dec(my_average(1, 2, 3))
# print(j)
# 神奇！！！！
# print(my_sum(1, 2, 34, '3'))
# print(my_sum(1, 2, 3, 4))
