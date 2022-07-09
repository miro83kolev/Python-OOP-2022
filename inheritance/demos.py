class Person: #person is extended by teacher
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}; Age:{self.age}'


class Teacher(Person): #teacher extends person
    def teach(self):
        print(f'Mr. {self.name} is teaching')

    def __str__(self):
        return f'{super().__str__()}'


t = Teacher("Miro", 39)
print(t.name)
print(t.age)

#self means instance
#super() means this instance from Parent