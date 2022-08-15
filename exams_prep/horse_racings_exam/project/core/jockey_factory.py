from project.jockey import Jockey


class JockeyFactory:

    @staticmethod
    def create_jockey(name, age):
        return Jockey(name, age)