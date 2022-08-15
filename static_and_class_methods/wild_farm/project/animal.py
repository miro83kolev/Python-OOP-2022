from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name, age, gender):
        self.gender = gender
        self.age = age
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


