from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.core.validator import Validator
from project.drink.drink import Drink


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        Validator.check_if_value_is_less_than_zero(value, 'Capacity has to be greater than 0!')
        self.__capacity = value

    def reserve(self, number_of_people: int):
        # change to reserved
        self.is_reserved = True
        # num of people added to table
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        # adding food to order
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        # adding drink to order
        self.drink_orders.append(drink)

    def get_bill(self):
        # get total of food price
        total_food_price = [food.price for food in self.food_orders]
        # get total of drink price
        total_drink_price = [drink.price for drink in self.drink_orders]
        return total_food_price + total_drink_price

    def clear(self):
        # move back to not reserved
        self.is_reserved = False
        # clear food orders
        self.food_orders.clear()
        # clear drink orders
        self.drink_orders.clear()
        # clear number of people on table
        self.number_of_people = 0

    def free_table_info(self):
        # check if it is reserved
        if not self.is_reserved:
            return f"Table: {self.table_number}\nType: {self.__class__.__name__}\nCapacity: {self.capacity}"