class Validator:
    @staticmethod
    def validate_if_not_empty_string(string, message):
        if string == '':
            raise ValueError(message)

    @staticmethod
    def validate_if_num_less_than_zero(number, message):
        if number < 0:
            raise ValueError(message)
