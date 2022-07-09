class Person:
    min_age = 0 # field(data attribute)

    #self is 'this' in Java, C#, JS,

    def __init__(self, name: str, age: int): # method (function attribute)
        self.name = name #property, field(data attribute)
        self.age = age #property, field(data attribute)

    def print_info(self): # method (function attribute)
        print(f'I am {self.name} and I am {self.age} years old.')

    def equals(self, other): # method (function attribute)
        print(self == other)


p1 = Person('Miro', 39) # 1st instance of a class 
p2 = Person('Niki', 5) # 2nd instance of a class
p1.print_info()
p2.print_info()



