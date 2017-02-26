def set_passline(passline):
    def comp(val):
        if val >= passline:
            print("pass")
        else:
            print('failed')

    return comp


f = set_passline(60)
f(89)
f = set_passline(90)
f(89)
