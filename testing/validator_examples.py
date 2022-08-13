class Validator:
    @staticmethod
    # check and raise if empty str
    def raise_if_string_is_empty(string, message):
        if not string:
            raise ValueError(message)

    # check and raise if value is less than zero
    @staticmethod
    def raise_if_price_is_negative_or_zero(value, message):
        if value <= 0:
            raise ValueError(message)

    # check and validate a type inside a list of valid types
    @staticmethod
    def validate_fish_type(fish_type):
        valid_fish_types = ["FreshwaterFish", "SaltwaterFish"]
        if fish_type not in valid_fish_types:
            return False
        return True

    # checks if not empty str or white space
    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string, message):
        if string.strip() == "":
            raise ValueError(message)

    # checks if inside a range
    @staticmethod
    def raise_if_inside_table_number_outside_of_range(value, message):
        if not 1 <= value <= 50:
            raise ValueError(message)

    # checks if it exists certain name in list raise error message
    @staticmethod
    def raise_if_food_already_exists(food_menu, food_name, message):
        for food in food_menu:
            if food.name == food_name:
                raise Exception(message)

    # check and raise if less symbols than required
    @staticmethod
    def raise_if_model_is_less_than_min_symbols(value, min_length, message):
        if len(value) < min_length:
            raise ValueError(message)

    # find a thing in list by using a stack
    @staticmethod
    def find_available_car(cars, car_type, message):
        for index in range(len(cars) - 1, -1, -1):
            car = cars[index]
            if car.__class__.__name__ == car_type and not car.is_taken:
                return car
        raise Exception(message)

    # find by name in list if not raise error
    @staticmethod
    def find_driver_by_name(drivers, driver_name, message):
        for driver in drivers:
            if driver.name == driver_name:
                return driver
        raise Exception(message)

    # minimum requirement for something
    @staticmethod
    def raise_if_not_enough_drivers_in_race(race, min_drivers, message):
        if len(race.drivers) < min_drivers:
            raise Exception(message)

    # if some instance attr is none
    @staticmethod
    def raise_if_driver_doesnt_have_a_car(driver, message):
        if driver.car is None:
            raise Exception(message)

    # raises if less than min value
    @staticmethod
    def raise_if_value_is_less_than_min_value(value, min_value, message):
        if value < min_value:
            raise ValueError(message)

    # raises if value in min max range
    @staticmethod
    def raise_if_value_out_if_range(value, min_value, max_value, message):
        if not min_value <= value <= max_value:
            raise ValueError(message)

    # checks if name in a list of names if not exception
    @staticmethod
    def raise_if_player_name_exists(player_names, player_name, message):
        if player_name in player_names:
            raise Exception(message)

    # checks if supply is avalable, error messages in dict, idx supplies
    @staticmethod
    def raise_if_supply_type_is_not_available(supplies, supply_type):
        messages_by_supply_type = {
            "Food": "There are no food supplies left!",
            "Drink": "There are no drink supplies left!"
        }

        for index in range(len(supplies) - 1, -1, -1):
            supply = supplies[index]
            if supply.__class__.__name__ == supply_type:
                return supplies.pop(index)

        raise Exception(messages_by_supply_type[supply_type])

    # raises if not correct object type
    @staticmethod
    def raise_if_object_not_correct_type(value, object_type, message):
        if not value.__class__.__name__ == object_type:
            raise ValueError(message)

    # raises if exist in a collection of things
    @staticmethod
    def raise_if_username_exists(users_collection, username, message):
        if any([user.username == username for user in users_collection]):
            raise Exception(message)






