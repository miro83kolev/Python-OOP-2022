from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def max_speed(self):
        return 140

    def train(self):
        if self.speed < self.max_speed:
            self.speed += 3
        else:
            raise Exception('Horse speed is too high!')