import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, point): #instance related method
        return math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)

    @staticmethod #declaring a staticmethod with decorator
    def calc_distance(p1, p2):
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)



p = Point(5, 6)
p1 = Point(3,4)
p.calculate_distance(p1)
Point.calc_distance() #access static method