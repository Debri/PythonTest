def deco(func):
    def in_deco(a, b):
        print('in_deco')
        func(a, b)

    print('deco')
    # return in_deco
    return in_deco

@deco
def bar(x, y):
    print('bar', x + y)

bar(1, 2)
print(type(bar))
print(bar.__class__)
# amazing!!!
