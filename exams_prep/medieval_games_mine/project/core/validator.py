class Validator:

    @staticmethod
    def check_for_empty_string_raises_value_error(string, message):
        if string == "":
            raise ValueError(message)

    @staticmethod
    def check_if_value_is_less_than_zero(number, message):
        if number < 0:
            raise ValueError(message)

    @staticmethod
    def check_if_name_in_list_of_players(players, player_name, message):
        if player_name in players:
            raise Exception(message)

    @staticmethod
    def check_if_value_below_min_value(value, min_value, message):
        if value < min_value:
            raise ValueError(message)

    @staticmethod
    def check_in_range_between_min_max_value(value, min_value, max_value, message):
        if not min_value <= value <= max_value:
            raise ValueError(message)

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