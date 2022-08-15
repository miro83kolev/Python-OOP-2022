class Validator:
    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string, message): # validates string
        if string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_astronaut_type_is_not_valid(valid_astronaut_types, astronaut_type, message): # validates object type
        if astronaut_type not in valid_astronaut_types:
            raise Exception(message)

    @staticmethod
    def raise_if_astronaut_doesnt_exist(astronaut_repository, name, message): # checks if astronaut part of repo
        if not astronaut_repository.find_by_name(name):
            raise Exception(message)

    @staticmethod
    def raise_if_planet_doesnt_exist(planet_repository, name, message): # checks if planet part of repo
        if not planet_repository.find_by_name(name):
            raise Exception(message)

    @staticmethod
    def raise_if_not_suitable_astronauts(astronaut_repository, message): #checks if astronaut suitable for mission
        if not any([ast.oxygen > 30 for ast in astronaut_repository.astronauts]):
            raise Exception(message)