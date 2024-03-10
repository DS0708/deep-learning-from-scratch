class Man:
    def __init__(self, name):       # Constructor
        self.name = name
        print("Initializing Man")

    def hello(self):
        print("Hello "+self.name+"!")

    def goodbye(self):
        print("Goodbye "+self.name+"!")

m = Man("DS")
m.hello()
m.goodbye()