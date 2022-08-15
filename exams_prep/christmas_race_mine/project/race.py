from project.core.validator import Validator


class Race:
    def __init__(self, name: str):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_if_no_whitespace_or_empty_string(value, "Name cannot be an empty string!")
        self.__name = value
