from project.reptile import Reptile


class Snake(Reptile):
    def __init__(self, name):
        super(Reptile, self).__init__(name)