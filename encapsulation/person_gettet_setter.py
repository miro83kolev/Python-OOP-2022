class Person:
    def __init__(self, age=0):
        self.age = age #be careful if you change here to __age it won't work you should change it in getter and setter

    @property # also called getter
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            self.__age = 18
        else:
            self.__age = age

    #props and tab autocompletes getter, setter


person = Person(25)
print(person.age)
person.age = 10
print(person.age)