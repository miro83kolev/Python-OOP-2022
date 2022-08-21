from project.planet.planet import Planet


class PlanetFactory:
    @staticmethod
    def create_planet(name, items):
        # creates a planet using planet class
        planet = Planet(name)
        # creates items on the planet a list
        planet.items = (items.split(", "))
        return planet
