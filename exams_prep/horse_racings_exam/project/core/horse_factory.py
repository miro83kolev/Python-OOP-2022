from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class HorseFactory:
    valid_horses_types = {
        'Appaloosa': Appaloosa,
        'Thoroughbred': Thoroughbred
    }

    @staticmethod
    def create_horse(horse_type, name, speed):
        return HorseFactory.valid_horses_types[horse_type](name, speed)
