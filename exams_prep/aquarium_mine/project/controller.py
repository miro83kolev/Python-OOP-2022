from project.core.aquarium_factory import AquariumFactory
from project.core.decoration_factory import DecorationFactory
from project.core.fish_factory import FishFactory
from project.core.validator import Validator
from project.decoration.decoration_repository import DecorationRepository


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        # using from validator checks for valid aquarium type
        if not Validator.validate_aquarium_type(aquarium_type):
            return "Invalid aquarium type."
        # creates an aquarium
        aquarium = AquariumFactory.create_aquarium(aquarium_type, aquarium_name)
        self.aquariums.append(aquarium)

        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        # using from validator checks for valid decoration type
        if not Validator.validate_decoration_type(decoration_type):
            return "Invalid decoration type."
        # creates a decoration
        decoration = DecorationFactory.create_decoration(decoration_type)
        self.decorations_repository.add(decoration)

        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        # finds by type decoration in repo using method
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = self.find_aquarium_by_name(aquarium_name)

        if aquarium is not None:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def find_aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
        return None

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        # using from validator checks for valid fish type
        if not Validator.validate_fish_type(fish_type):
            return f"There isn't a fish of type {fish_type}."
        # creates a fish
        fish = FishFactory.create_fish(fish_type, fish_name, fish_species, price)
        aquarium = self.find_aquarium_by_name(aquarium_name)

        if aquarium is not None:
            return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.find_aquarium_by_name(aquarium_name)

        if aquarium is not None:
            aquarium.feed()
            return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        sum_decorations = sum([d.price for d in aquarium.decorations])
        sum_fish = sum([f.price for f in aquarium.fish])
        total_value = sum_decorations + sum_fish

        return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."

    def report(self):
        output = ""

        for aquarium in self.aquariums:
            output += str(aquarium)

        return output.strip()