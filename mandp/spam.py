def spam1():

    def spam2():

        def spam3():
            z="Even "
            z += y
            print("In spam 3: {}".format(locals()))
            return z

        y = "more " + x
        y += spam3()
        print("In spam 2: {}".format(locals()))
        return y


    x = "spam "
    x += spam2()
    print("In spam 1: {}".format(locals()))
    return x

print(spam1())