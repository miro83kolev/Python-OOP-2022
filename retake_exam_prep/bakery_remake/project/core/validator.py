class Validator:
    # checks if value is empty str or whitespace
    @staticmethod
    def check_if_empty_string_or_whitespace(value, message):
        if value.strip() == '':
            raise ValueError(message)

    # checks if value less than zero
    @staticmethod
    def check_if_value_is_less_than_zero(value, message):
        if value <= 0:
            raise ValueError(message)

    # checks if outside table in required range
    @staticmethod
    def check_if_outside_table_in_range(value, message):
        if not 51 <= value <= 100:
            raise ValueError(message)

    # checks if inside table in required range
    @staticmethod
    def check_if_inside_table_in_range(value, message):
        if not 1 <= value <= 50:
            raise ValueError(message)

    # checks if food already exists in food menu and if raises ex
    @staticmethod
    def check_if_food_already_exists(food_menu, food_name, message):
        for food in food_menu:
            if food.name == food_name:
                raise Exception(message)

    # checks if drink already exists in drinks menu and if raises ex
    @staticmethod
    def check_if_drink_already_exists(drink_menu, drink_name, message):
        for drink in drink_menu:
            if drink.name == drink_name:
                raise Exception(message)

    # checks if table already exists in table repo and if raises ex
    @staticmethod
    def check_if_table_already_exists(tables, table_number, message):
        for table in tables:
            if table.table_number == table_number:
                raise Exception(message)

