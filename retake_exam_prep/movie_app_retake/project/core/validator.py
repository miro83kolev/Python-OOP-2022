class Validator:
    @staticmethod
    def check_if_string_is_not_empty(value, message):
        if value == '':
            raise ValueError(message)

    @staticmethod
    def check_if_value_below_min_value(value, min_value, message):
        if value < min_value:
            raise ValueError(message)

    @staticmethod
    def check_if_obj_correct_type(value, obj_type, message):
        if not value.__class__.__name__ == obj_type:
            raise ValueError(message)

    # try to find any user that has this name
    @staticmethod
    def check_if_user_name_exists(users, username, message):
        if any(user.username == username for user in users):
            raise ValueError(message)

    # try to find any user does not have this name
    @staticmethod
    def check_if_user_name_does_not_exists(users, username, message):
        if not any(user.username == username for user in users):
            raise ValueError(message)

    # checks if username not a movie owner
    @staticmethod
    def check_if_username_is_not_movie_owner(movie, username, message):
        if not movie.owner.username == username:
            raise Exception(message)

    # checks if username is a movie owner
    @staticmethod
    def check_if_username_is_movie_owner(movie, username, message):
        if movie.owner.username == username:
            raise Exception(message)

    # checks if user liked a movie
    @staticmethod
    def check_if_movie_already_liked_by_user(user, movie, message):
        if movie in user.movies_liked:
            raise Exception(message)

    # checks if user does not like a movie
    @staticmethod
    def check_if_movie_not_liked_by_user(user, movie, message):
        if movie not in user.movies_liked:
            raise Exception(message)

    # checks if move already inside a movie collection
    @staticmethod
    def check_if_movie_already_in_collection(movies_collection, movie, message):
        if movie in movies_collection:
            raise Exception(message)

    # checks if move is not inside a movie collection
    @staticmethod
    def check_if_movie_not_in_collection(movies_collection, movie, message):
        if movie not in movies_collection:
            raise Exception(message)



