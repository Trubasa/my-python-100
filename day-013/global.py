x = 1


def toast():
    x = 2
    def toast2():
        global x
        x = 3
    toast2()


toast()
print(x)
