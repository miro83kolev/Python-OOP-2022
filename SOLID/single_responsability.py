#single responsibility - valid for method, class, module


def sum2(numbers):
    the_sum = sum(numbers)
    print(the_sum)

#no single responsibility, should be separated in 2 methods


class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    #violation is also doing it for 2 shapes
    def print_triangle_area(self):
        area = self.width * self.height / 2
        print(area) # SPR violation

    def print_rectangle_area(self):
        area = self.width * self.height
        print(area) # SPR violation

tr = Shape(10, 5)
rec = Shape(10, 5)

tr.print_triangle_area()
rec.print_rectangle_area()




