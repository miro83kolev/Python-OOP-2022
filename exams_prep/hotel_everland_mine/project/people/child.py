class Child:
    def __init__(self, food_cost: int, *toys_cost):
        self.cost = sum(toys_cost) + food_cost # total cost of all toys cost + food cost

    def get_monthly_expense(self):
        return self.cost * 30
