from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod # no definition on method, just abstraction
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

# no definition of class and implementing methods


class Circle(Shape):
    def __init__(self, r):
        self.__radius = r

    def calculate_area(self):
        return math.pi * self.__radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
