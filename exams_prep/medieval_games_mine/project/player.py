from project.core.validator import Validator


class Player:
    used_names = set()

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_for_empty_string_raises_value_error(value, 'Name not valid!')
        Validator.check_if_name_in_list_of_players(Player.used_names, value, f'Name {value} is already used!')
        self.__name = value
        Player.used_names.add(value)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.check_if_value_below_min_value(value, 12, 'The player cannot be under 12 years old!')
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        Validator.check_in_range_between_min_max_value(value, 0, 100, 'Stamina not valid!')
        self.__stamina = value
    
    @property
    def need_sustenance(self):
        return self.stamina < 100

    def __str__(self):
        return f'Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}'

    def __gt__(self, other):
        return self.stamina > other.stamina

