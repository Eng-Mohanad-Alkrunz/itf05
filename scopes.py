print("Hellp")
a = 50

def outer_function():
    # global a
    globals()['a'] = 60
    a = 20
    print("Hellp")

    def inner_function():
        nonlocal a
        # print("Before Change a = ",a)
        #
        a += 1
        # # a = 30
        print("a value from inner function", a)

    inner_function()
    print("a value from outer function",a)

outer_function()
print("a value from global scope",a)
