class Validator:
    @staticmethod
    def raise_white_space_or_empty_str(string, message):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_float_0_or_less(number, message):
        if number <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_not_in_range(number, min_value, max_value, message):
        if number < min_value or number > max_value:
            raise ValueError(message)

