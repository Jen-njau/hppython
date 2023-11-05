class cars:
    # constructor
    def __init__(self, type, color, model):
        self.type = type
        self.color = color
        self.model = model
    # method
    def onyesha (self):
        print(f"i love {self.model} cars which is a {self.type} being {self.color}")

# create object
myobj = cars("saloon","White","Toyota")
myobj.onyesha()
myobj2 = cars("s.wagon","black","mazda")
myobj2.onyesha()

