from Tools.scripts.treesync import raw_input


def test(str):
    print(str)
    return


test("1111111111")
test("123")


def change(mylist):
    mylist[0] = 123
    print(mylist)
    return


list = [2, 4, 65, 45]
change(list)


def printinfo(arg1, *var):
    print(arg1)
    for varss in var:
        print(varss)
    return


sum = lambda a, b: a + b
print(sum(1, 2))
# printinfo(123)
# printinfo(12, 23, 23)
str = raw_input("shiru: ")
print(str)
str1=input("zaicishuru : ")
print(str1)