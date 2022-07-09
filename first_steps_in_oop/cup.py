class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def status(self):
        return self.size - self.quantity

    def fill(self, millitters):
        if self.status() >= millitters: #calling self.status function for this instance inside the class
            self.quantity += millitters


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())



