from abc import ABC, abstractmethod

from project.core.validator import Validator


class Astronaut(ABC):
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_if_empty_string_or_whitespace(value, 'Astronaut name cannot be empty string or whitespace!')
        self.__name = value

    @abstractmethod
    def breathe(self):
         self.oxygen -= 10

    def increase_oxygen(self, amount: int):
        self.oxygen += amount



