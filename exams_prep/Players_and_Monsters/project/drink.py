from project.product import Product

class Drink(Product):
     #DEFAULT_QUANTITY = 10
     def __init__(self, name, ):
          super().__init__(name, 10) #self.DEFAULT_QUANTITY