class Validator:
    @staticmethod
    def check_if_string_is_not_empty(value, message):
        if value == '':
            raise ValueError(message)

    @staticmethod
    def check_if_value_is_less_than_zero(value, message):
        if value < 0:
            raise ValueError(message)

    @staticmethod
    def check_if_name_not_used(player_names, player_name, message):
        if player_name in player_names:
            raise Exception(message)

    @staticmethod
    def check_if_value_under_min_value(value, min_value, message):
        if value < min_value:
            raise ValueError(message)

    @staticmethod
    def check_if_value_in_range_min_max_value(value, min_value, max_value, message):
        if not min_value <= value <= max_value:
            raise ValueError(message)

    @staticmethod
    def check_if_supply_type_is_not_available(supplies, supply_type):
        # dict mapper of messages
        messages_by_supply_type = {
            "Food": "There are no food supplies left!",
            "Drink": "There are no drink supplies left!"
        }
        # iterates backwards - stack
        for index in range(len(supplies) - 1, -1, -1):
            supply = supplies[index]
            if supply.__class__.__name__ == supply_type:
                return supplies.pop(index)

        raise Exception(messages_by_supply_type[supply_type])
