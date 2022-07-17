from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError('Cannot set name less then 2 chars')
        self.__name = value

class Cat(Animal):
    def __init__(self, name, layziness):
        super().__init__(name)
        self.layziness = layziness

    def make_sound(self):
        return 'meow'

class Dog(Animal):
    def make_sound(self):
        return 'bau bau'
    

cat = Cat('Tony', 10)
dog = Dog('Jonny')

print(dog.name)
print(cat.name)
print(cat.layziness)
print(cat.make_sound())
print(dog.make_sound())



