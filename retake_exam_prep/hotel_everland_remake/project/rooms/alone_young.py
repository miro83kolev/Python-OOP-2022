from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, 1)
        self.room_cost = 10
        # adds the tv appliance to list of appliances
        self.appliances = [TV()]
        # calculates the expenses for these appliances
        self.calculate_expenses(self.appliances)
