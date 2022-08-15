from abc import ABC, abstractmethod

from project.core.validator import Validator


class Horse(ABC):
    MAX_SPEED = 0 # set up max speed of 0 to be changed in child class

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_if_under_required_len_of_symbols(value, 4, 'Horse name {value} is less than 4 symbols!')
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        Validator.check_if_over_required_speed(value, self.MAX_SPEED, 'Horse speed is too high!')
        self.__speed = value

    @abstractmethod
    def train(self):
        pass

