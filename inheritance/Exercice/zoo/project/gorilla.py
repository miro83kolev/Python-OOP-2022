from project.mammal import Mammal


class Gorilla(Mammal):
    def __init__(self, name):
        super(Mammal, self).__init__(name)