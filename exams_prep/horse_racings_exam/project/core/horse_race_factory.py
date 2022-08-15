from project.horse_race import HorseRace


class HorseRaceFactory:
    @staticmethod
    def create_horse_race(race_type):
        return HorseRace(race_type)