from project.user import User


class UserFactory:
    # using user class to create a user
    @staticmethod
    def create_user(username, age):
        return User(username, age)
