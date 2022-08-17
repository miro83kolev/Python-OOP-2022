from project.rooms.room import Room


class Everland:
    # constructor empty list of rooms
    def __init__(self):
        self.rooms = []

    # adds room to list
    def add_room(self, room: Room):
        self.rooms.append(room)

    # getting monthly consumption
    def get_monthly_consumptions(self):
        # first total consumption is 0
        total_consumption = 0
        # for each room in rooms list
        for room in self.rooms:
            # to total consumption we add room expenses and room cost
            total_consumption += room.expenses + room.room_cost
        return f"Monthly consumption: {total_consumption:.2f}$."

    # pay method
    def pay(self):
        # empty list output
        output = []
        # for each room in rooms
        for room in self.rooms:
            # to total consumption we add room expenses and room cost
            total_expenses = room.expenses + room.room_cost
            # if room budget is greater or equal
            if room.budget >= total_expenses:
                # we subtract total expenses
                room.budget -= total_expenses
                # we add to output list
                output.append(f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                # otherwise
                output.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return "\n".join(output)

    # status method
    def status(self):
        # total room population is sum or each room members count in rooms list
        total_population = sum([room.members_count for room in self.rooms])
        output = f"Total population: {total_population}\n"
        # for each room
        for room in self.rooms:
            output += f"{room.family_name} with {room.members_count} members." \
                      f" Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            child_count = 1
            # for each child
            for child in room.children:
                output += f"--- Child {child_count} monthly cost: {child.get_monthly_expense():.2f}$\n"
                child_count += 1
            # if room has attribute called appliances
            if hasattr(room, "appliances"):
                output += f"--- Appliances monthly cost:" \
                          f" {sum([app.get_monthly_expense() for app in room.appliances]):.2f}$\n"
        return output.strip()
