from project.core.user_factory import UserFactory
from project.core.validator import Validator
from project.movie_specification.movie import Movie


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        # using validator static method checks if user already exists
        Validator.check_if_user_name_exists(self.users_collection, username, f'User already exists!')
        # creates a user if does not exist
        user = UserFactory.create_user(username, age)
        self.users_collection.append(user)
        return f'{username} registered successfully.'

    def __find_user_by_name(self, username):
        return [user for user in self.users_collection if user.username == username]

    def upload_movie(self, username: str, movie: Movie):
        # first using validator we check if username does not exist
        Validator.check_if_user_name_does_not_exists(self.users_collection, username, f'This user does not exist!')
        # second we check if username is owner of this movie or not
        Validator.check_if_username_is_not_movie_owner(movie, username,
                                                       f'{username} is not the owner of the movie {movie.title}!')
        # third we check if the movie is not already in this collection of movies
        Validator.check_if_movie_already_in_collection(self.movies_collection, movie,
                                                       f'Movie already added to the collection!')

        # finally if all checks pass we search user by username, we add movie to his collections
        user = self.__find_user_by_name(username)
        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f'{username} successfully added {movie.title} movie.'

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        # first we check if movie not in movies_collection
        Validator.check_if_movie_not_in_collection(self.movies_collection, movie,
                                                   f'The movie {movie.title} is not uploaded!')
        # second check if username is not the movie owner
        Validator.check_if_username_is_movie_owner(movie, username,
                                                   f'{username} is not the owner of the movie {movie.title}!')

        # if all checks pass we set attribute using this function

        for attribute, new_value in kwargs.items():
            setattr(movie, attribute, new_value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        # first we check if movie not in movies_collection
        Validator.check_if_movie_not_in_collection(self.movies_collection, movie,
                                                   f'The movie {movie.title} is not uploaded!')
        # second check if username is not the movie owner
        Validator.check_if_username_is_movie_owner(movie, username,
                                                   f'{username} is not the owner of the movie {movie.title}!')

        # finally if all checks pass we search user by username, we remove movie from his collections
        user = self.__find_user_by_name(username)
        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f'{username} successfully deleted {movie.title} movie.'

    def like_movie(self, username: str, movie: Movie):
        # first find user by name
        user = self.__find_user_by_name(username)
        # checks if the user is not the movie owner
        Validator.check_if_username_is_movie_owner(movie, username,
                                                   f'{username} is the owner of the movie {movie.title}!')
        # checks if the user has not already liked the movie
        Validator.check_if_movie_already_liked_by_user(user, movie,
                                                       f'{username} already liked the movie {movie.title}!')
        # after all checks
        movie.likes += 1
        user.movies_liked.append(movie)
        return f'{username} liked {movie.title} movie.'

    def dislike_movie(self, username: str, movie: Movie):
        # first find user by name
        user = self.__find_user_by_name(username)
        # checks if the user has not already disliked the movie
        Validator.check_if_movie_not_liked_by_user(user, movie, f'{username} has not liked the movie {movie.title}!')
        # after all checks
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f'{username} disliked {movie.title} movie.'

    def display_movies(self):
        # sorts movies by year first and then by title
        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        # if not in the collection
        if not self.movies_collection:
            return "No movies found."

        # otherwise iterate thru sorted movies collection and add each movie details
        output = ""
        for movie in sorted_movies:
            output += movie.details() + "\n"

        return output.strip()

    def __str__(self):
        output = "All users: "
        if not self.users_collection:
            output += "No users.\n"
        else:
            output += ', '.join([user.username for user in self.users_collection]) + '\n'

        output += "All movies: "
        if not self.movies_collection:
            output += "No movies.\n"
        else:
            output += ', '.join([movie.title for movie in self.movies_collection])

        return output.strip()









