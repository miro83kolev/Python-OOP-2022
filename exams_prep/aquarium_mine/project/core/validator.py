class Validator:
    # checks if a string is empty
    @staticmethod
    def raise_if_string_is_empty(string, message):
        if not string:
            raise ValueError(message)

    # checks if price is zero or negative
    @staticmethod
    def raise_if_price_is_negative_or_zero(value, message):
        if value <= 0:
            raise ValueError(message)

    # validates fish type from list of types
    @staticmethod
    def validate_fish_type(fish_type):
        valid_fish_types = ["FreshwaterFish", "SaltwaterFish"]
        if fish_type not in valid_fish_types:
            return False
        return True

    # validates decoration type from list of types
    @staticmethod
    def validate_decoration_type(decoration_type):
        valid_decoration_types = ["Ornament", "Plant"]
        if decoration_type not in valid_decoration_types:
            return False
        return True

    # validates aquarium type from list of types
    @staticmethod
    def validate_aquarium_type(aquarium_type):
        valid_aquarium_types = ["FreshwaterAquarium", "SaltwaterAquarium"]
        if aquarium_type not in valid_aquarium_types:
            return False
        return True
