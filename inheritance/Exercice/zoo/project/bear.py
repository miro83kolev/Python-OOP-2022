from project.mammal import Mammal


class Bear(Mammal):
    def __init__(self, name):
        super(Mammal, self).__init__(name)