from project.movie import Movie
from unittest import TestCase, main

class MovieTests(TestCase):
    NAME = 'Shutter Island'
    YEAR = 2010
    RATING = 8

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test_init(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter_raises_when_empty_string(self):
        with self.assertRaises(ValueError) as error:
            self.movie.name = ''
        self.assertEqual('Name cannot be an empty string!', str(error.exception))

    def test_year_setter_raises_when_empty_string(self):
        with self.assertRaises(ValueError) as error:
            self.movie.year = 1886
        self.assertEqual('Year is not valid!', str(error.exception))

    def test_appends_actors_correctly(self):
        first_actor = 'Ivan'
        second_actor = 'Stamat'

        self.movie.add_actor(first_actor)
        self.movie.add_actor(second_actor)
        self.assertEqual([first_actor, second_actor], self.movie.actors)

    def test_duplicate_actor_error_message(self):
        actor_name = 'Pesho'
        self.movie.add_actor(actor_name)
        result = self.movie.add_actor(actor_name)
        self.assertEqual(f'{actor_name} is already added in the list of actors!', result)
        self.assertTrue(1, len(self.movie.actors))
        self.assertEqual([actor_name], self.movie.actors)

    def test_gt_movie_than_another_movie(self):
        another_movie_name = 'Matrix'
        another_movie = Movie(another_movie_name, 1999, self.RATING - 2)
        first_result = self.movie > another_movie
        second_result = another_movie > self.movie
        self.assertEqual(f'"{self.movie.name}" is better than "{another_movie_name}"', first_result)
        self.assertEqual(f'"{self.movie.name}" is better than "{another_movie_name}"', second_result)

    def test_repr_returns_correct_string(self):
        actors = ['Pesho', 'Gosho']
        self.movie.actors = actors
        actual_result = repr(self.movie)
        expected_result = f"Name: {self.NAME}\n" \
               f"Year of Release: {self.YEAR}\n" \
               f"Rating: {self.RATING:.2f}\n" \
               f"Cast: {', '.join(actors)}"
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
