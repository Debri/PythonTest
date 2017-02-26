def deco(func):
    def in_deco():
        print('in_deco')
        func()

    print('deco')
    # return in_deco
    return in_deco


@deco
def bar():
    print('bar')


# bar()
print(type(bar))
print(bar.__class__)
# amazing!!!
