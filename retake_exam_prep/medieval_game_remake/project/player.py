from project.core.validator import Validator


class Player:
    _used_names = set()

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_if_string_is_not_empty(value, 'Name not valid!')
        Validator.check_if_name_not_used(Player._used_names, value, f'Name {value} is already used!')
        Player._used_names.add(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.check_if_value_under_min_value(value, 12, 'The player cannot be under 12 years old!')
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        Validator.check_if_value_in_range_min_max_value(value, 0, 100, 'Stamina not valid!')
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < 100

    def __str__(self):
        return f'Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}'

    def __gt__(self, other):
        return self.stamina > other.stamina

