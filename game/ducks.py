class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Wee this is fun")
        elif self.ratio == 1:
            print("This is hard work but i'm flying")
        else:
            print("I think i'll just walk")

class Duck(object):

    def __init__(self):
        self.wing = Wing(1.8)

    def walk(self):
        print("Waddle, Waddle, Waddle.")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack, Quack")

    def fly(self):
        self.wing.fly()

# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()

class penguin(object):

    def walk(self):
        print("Waddle, waddle, i waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far south")

    def quack(self):
        print("are you having a laugh? I'm a penguin")


if __name__ == '__main__':
    donald = Duck()
    donald.fly()




    # test_duck(donald)
    # Percy = penguin()
    # test_duck(Percy)