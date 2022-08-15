from project.core.horse_factory import HorseFactory
from project.core.horse_race_factory import HorseRaceFactory
from project.core.jockey_factory import JockeyFactory
from project.core.validator import Validator


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        valid_horse_types = ["Appaloosa", "Thoroughbred"]
        if horse_type in valid_horse_types:
            Validator.raise_if_name_already_exists_in_collection(self.horses, horse_name, f'Horse {horse_name} has been already added!')
            horse = HorseFactory.create_horse(horse_type, horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        Validator.raise_if_name_already_exists_in_collection(self.jockeys, jockey_name, f'Jockey {jockey_name} has been already added!')
        jockey = JockeyFactory.create_jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f'Jockey {jockey_name} has been already added!'

    def create_horse_race(self, race_type: str):
        created_races = set()
        Validator.raise_if_race_type_already_exists(created_races, race_type, f'Race {race_type} has been already created!')
        race = HorseRaceFactory.create_horse_race(race_type)
        created_races.add(race)
        return f'Race {race_type} is created.'

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = Validator.find_available_jockey_raise_if_none(self.jockeys, jockey_name, f"Jockey {jockey_name} could not be found!")
        horse = Validator.find_available_horse_raise_if_none(self.horses, horse_type, f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f'Jockey {jockey_name} already has a horse.'
        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey = Validator.find_available_jockey_raise_if_none(self.jockeys, jockey_name, f"Jockey {jockey_name} could not be found!")
        race = Validator.find_available_race_raise_if_none(self.horse_races, race_type, f'Race {race_type} could not be found!')

        if any([j.name == jockey_name for j in race.jockeys]):
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = Validator.find_available_race_raise_if_none(self.horse_races, race_type, f'Race {race_type} could not be found!')
        Validator.raise_if_not_enough_jockeys_in_race(race_type, 2, 'Horse race {race_type} needs at least two participants!')

        racers = sorted(race.jockeys, key=lambda x: -x.horse.speed)
        winner = racers[0]
        output = ""

        for jockey in racers:
            output += f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."

        return output.strip()
