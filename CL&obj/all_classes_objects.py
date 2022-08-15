class Person:
    #dunder init = double underscore == dunder initialize
    def __init__(self, name, age):
        self.name = name
        self.age = age

test_person = Person("John", 5)
print(test_person.age)
print(test_person.name)

