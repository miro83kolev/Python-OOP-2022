from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    #one young person, 1 salary, room cost 10, added 1 tv + calculate_expenses method
    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, 1)
        self.room_cost = 10
        self.appliances = [TV()]
        self.calculate_expenses(self.appliances)