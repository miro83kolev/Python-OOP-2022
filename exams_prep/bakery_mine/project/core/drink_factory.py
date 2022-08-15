from project.drink.tea import Tea
from project.drink.water import Water


class DrinkFactory:
    #drinks mapper - a dict
    drink_types = {
        "Tea": Tea,
        "Water": Water
    }

    @staticmethod
    def create_drink(drink_type, name, portion, brand):
        return DrinkFactory.drink_types[drink_type](name, portion, brand)