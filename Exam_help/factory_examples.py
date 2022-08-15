class AquariumFactory:
    # dict mapper of other classes types
    aquarium_types = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium
    }

    # creates an object with given type and name
    @staticmethod
    def create_aquarium(aquarium_type: str, aquarium_name: str):
        return AquariumFactory.aquarium_types[aquarium_type](aquarium_name)

    # creates an object and its items split by ,
    @staticmethod
    def create_planet(name, items):
        planet = Planet(name)
        planet.items = (items.split(", "))
        return planet