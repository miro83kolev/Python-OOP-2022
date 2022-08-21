from abc import ABC, abstractmethod

from project.core.validator import Validator


class Supply(ABC):
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_if_string_is_not_empty(value, 'Name cannot be an empty string.')
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        Validator.check_if_value_is_less_than_zero(value, 'Energy cannot be less than zero.')
        self.__energy = value

    @abstractmethod
    def details(self):
        pass

