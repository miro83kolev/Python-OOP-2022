from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120 # changed max speed in child class

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        try:
            self.speed += 2 # try to add if possible else error and speed equal to max speed
        except ValueError:
            self.speed = self.MAX_SPEED
