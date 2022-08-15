class Validator:
    # checks if empty string or whitespace
    @staticmethod
    def check_if_empty_string_or_whitespace(string, message):
        if string.strip() == '':
            raise ValueError(message)

    # checks if value is under min value
    @staticmethod
    def check_if_value_under_min_value(value, min_value, message):
        if value < min_value:
            raise ValueError(message)

    # checks if value is under required length
    @staticmethod
    def check_if_under_required_len_of_symbols(value, min_len, message):
        if len(value) < min_len:
            raise ValueError(message)

    # checks if value is over required max
    @staticmethod
    def check_if_over_required_speed(value, max_speed, message):
        if value > max_speed:
            raise ValueError(message)

    # checks if valid race type is given
    @staticmethod
    def check_if_race_is_valid_type(race_type, message):
        valid_race_types = ["Winter", "Spring", "Autumn", "Summer"]
        if race_type not in valid_race_types:
            raise ValueError(message)

    # checks if any object.name in obj collection has the same as parameter name
    @staticmethod
    def raise_if_name_already_exists_in_collection(collection, name, message):
        if any([obj.name == name for obj in collection]):
            raise Exception(message)

    # checks if any object.type in obj collection has the same as parameter name
    @staticmethod
    def raise_if_race_type_already_exists(collection, race_type, message):
        if any([obj.race_type == race_type for obj in collection]):
            raise Exception(message)

    # checks if available jockey by name
    @staticmethod
    def find_available_jockey_raise_if_none(jockeys, name, message):
        for j in jockeys:
            if j.name == name:
                return j
        raise Exception(message)

    # checks for available horse inside horses collection backwards and verifies if horse is correct type by class and not taken
    @staticmethod
    def find_available_horse_raise_if_none(horses, horse_type, message):
        for idx in range(len(horses) - 1, -1, -1):
            horse = horses[idx]
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                return horse
        raise Exception(message)

    # checks if available race by type
    @staticmethod
    def find_available_race_raise_if_none(races, race_type, message):
        for race in races:
            if race.race_type == race_type:
                return race
        raise Exception(message)

    # checks if jockey does not have a horse
    @staticmethod
    def raise_if_jockey_doesnt_have_a_horse(jockey, message):
        if jockey.horse is None:
            raise Exception(message)

    # checks if not enough jockeys for race
    @staticmethod
    def raise_if_not_enough_jockeys_in_race(race, message):
        if len(race.jockeys) < 2:
            raise Exception(message)
