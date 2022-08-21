from project.drink.tea import Tea
from project.drink.water import Water


class DrinkFactory:
    # dict mapper of drink types
    drink_types = {
        "Tea": Tea,
        "Water": Water
    }

    # create drink method from drink type, name, portion, brand
    @staticmethod
    def create_drink(drink_type, name, portion, brand):
        return DrinkFactory.drink_types[drink_type](name, portion, brand)