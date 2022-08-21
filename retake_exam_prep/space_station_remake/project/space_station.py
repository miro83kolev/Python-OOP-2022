from collections import deque
from project.astronaut.astronaut_repository import AstronautRepository
from project.core.astronaut_factory import AstronautFactory
from project.core.planet_factory import PlanetFactory
from project.core.validator import Validator
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    successful_missions = 0
    not_successful_missions = 0

    def __init__(self):
        # create both repos using the repos classes
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        # checks if astro in repo with find_by_name method
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."
        # if not in: astro creation by its factory, add to list and return message
        astronaut = AstronautFactory.create_astronaut(astronaut_type, name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        # checks if planet in repo with find_by_name method
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        # if not in: planet creation by its factory, add to list and return message
        planet = PlanetFactory.create_planet(name, items)
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        # using validator we check if astro does not exist in astro repo
        Validator.check_if_astronaut_doesnt_exist(self.astronaut_repository, name, f"Astronaut {name} doesn't exist!")
        # if in repo: we find astro by using find_by_name method
        astronaut = self.astronaut_repository.find_by_name(name)
        # we remove and return message
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        # for each astro in repo we apply increase oxygen method
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        # using validator we check if planet exists in planet repo
        Validator.check_if_planet_doesnt_exist(self.planet_repository, planet_name, "Invalid planet name!")
        # using validator we check for suitable astros to send on mission
        Validator.check_if_not_suitable_astronauts(
            self.astronaut_repository,
            "You need at least one astronaut to explore the planet!")
        # if all checks passed we find a planet by name using the method
        planet = self.planet_repository.find_by_name(planet_name)
        # we sort astros by oxygen level
        sorted_astronauts = sorted(self.astronaut_repository.astronauts, key=lambda x: x.oxygen, reverse=True)
        # all suitable is a list of astros with more than 30 oxygen
        suitable_astronauts = [ast for ast in sorted_astronauts if ast.oxygen > 30]
        # we use the staticmethod explore planet to get result
        return SpaceStation.explore_planet(suitable_astronauts, planet)

    @staticmethod
    def explore_planet(astronauts, planet):
        # first 5 astros to be sent on mission
        astronauts = deque(astronauts[:5])
        items = planet.items
        astronauts_count = 1

        while items and astronauts:
            current_astronaut = astronauts[0]
            current_item = items.pop()

            current_astronaut.breathe()
            current_astronaut.backpack.append(current_item)
            if current_astronaut.oxygen <= 0:
                astronauts.popleft()
                astronauts_count += 1

        if items:
            SpaceStation.not_successful_missions += 1
            return "Mission is not completed."

        SpaceStation.successful_missions += 1
        return f"Planet: {planet.name} was explored. {astronauts_count} astronauts participated in collecting items."

    def report(self):
        output = f"{SpaceStation.successful_missions} successful missions!\n"
        output += f"{SpaceStation.not_successful_missions} missions were not completed!\n"
        output += f"Astronauts' info:\n"
        # for each astro in astro repo
        for astronaut in self.astronaut_repository.astronauts:
            backpack_items = "none" if not astronaut.backpack else ", ".join(astronaut.backpack)
            output += f"Name: {astronaut.name}\nOxygen: {astronaut.oxygen}\n"
            output += f"Backpack items: {backpack_items}\n"

        return output.strip()
