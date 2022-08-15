from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def max_speed(self):
        return 120

    def train(self):
        if self.speed < self.max_speed:
            self.speed += 2
        else:
            raise Exception('Horse speed is too high!')
