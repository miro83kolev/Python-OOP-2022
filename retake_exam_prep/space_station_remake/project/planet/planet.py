from project.core.validator import Validator


class Planet:
    def __init__(self, name):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_if_empty_string_or_whitespace(value, 'Planet name cannot be empty string or whitespace!')
        self.__name = value
