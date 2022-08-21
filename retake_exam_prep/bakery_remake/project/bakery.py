from project.core.drink_factory import DrinkFactory
from project.core.food_factory import FoodFactory
from project.core.table_factory import TableFactory
from project.core.validator import Validator


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_if_empty_string_or_whitespace(value, 'Name cannot be empty string or white space!')
        self.__name = value

    def add_food (self, food_type: str, name: str, price: float):
        # checks with validator
        Validator.check_if_food_already_exists(self.food_menu, name, f'{food_type} {name} is already in the menu!')

        #creates food
        food = FoodFactory.create_food(food_type, name, price)
        self.food_menu.append(food)
        return f'Added {name} ({food_type}) to the food menu'

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        # checks with validator
        Validator.check_if_drink_already_exists(self.drinks_menu, name, f'{drink_type} {name} is already in the menu!')
        # create a drink
        drink = DrinkFactory.create_drink(drink_type, name, portion, brand)
        self.drinks_menu.append(drink)
        return f'Added {name} ({brand}) to the drink menu'

    def dd_table(self, table_type: str, table_number: int, capacity: int):
        # checks with validator
        Validator.check_if_table_already_exists(self.tables_repository, table_number,
                                                'Table {table_number} is already in the bakery!')
        table = TableFactory.create_table(table_type, table_number, capacity)
        self.tables_repository.append(table)
        return f'Added table number {table_number} in the bakery'

    def reserve_table(self, number_of_people: int):
        # iterates throughout each table
        for table in self.tables_repository:
            # if it is not reserved and capacity allows it
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f'Table {table.table_number} has been reserved for {number_of_people} people'
        return f'No available table for {number_of_people} people'

    def order_food(self, table_number: int, *food_names):
        # using static method find table by number we find tables
        table = self.find_table_by_table_number(table_number)
        # if it is none
        if table is None:
            return f"Could not find table {table_number}"
        # ordered food
        ordered_food = f"Table {table_number} ordered:\n"
        non_existing_food = f"{self.name} does not have in the menu:\n"
        # iterates in food names args
        for food_name in food_names:
            # find food by its name
            food = Bakery.find_instance_by_name(food_name, self.food_menu)
            # if it is not none
            if food is not None:
                ordered_food += f"{repr(food)}\n"
                table.order_food(food)
            else:
                non_existing_food += f"{food_name}\n"
        # output collects both ordered and non existing food
        output = ordered_food + non_existing_food
        return output.strip()

    @staticmethod
    def find_instance_by_name(name, collection):
        for item in collection:
            if item.name == name:
                return item
        return None

    # instance method
    def find_table_by_table_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table
        return None

    # same as order food
    def order_drink(self, table_number: int, *drink_names):
        table = self.find_table_by_table_number(table_number)

        if table is None:
            return f"Could not find table {table_number}"

        ordered_drinks = f"Table {table_number} ordered:\n"
        non_existing_drinks = f"{self.name} does not have in the menu:\n"

        for drink_name in drink_names:
            drink = Bakery.find_instance_by_name(drink_name, self.drinks_menu)

            if drink is not None:
                ordered_drinks += f"{repr(drink)}\n"
                table.order_drink(drink)
            else:
                non_existing_drinks += f"{drink_name}\n"

        output = ordered_drinks + non_existing_drinks
        return output.strip()

    def leave_table(self, table_number: int):
        # find table by using instance method find table by number
        table = self.find_table_by_table_number(table_number)

        if table is not None:
            # get bill using this method from table class
            bill = table.get_bill()
            # clear table
            table.clear()
            # total income + bill
            self.total_income += bill
            return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        output = ""
        # iterates in tables repo
        for table in self.tables_repository:
            # if not reserved
            if not table.is_reserved:
                output += table.free_table_info() + "\n"

        return output.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"



