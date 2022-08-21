from project.movie import Movie

from unittest import TestCase, main


class MovieTests(TestCase):
    def setUp(self) -> None:
        self.movie = Movie('Test', 2002, 8.6)
        self.movie_two = Movie('Test2', 2001, 8.4)
        self.movie_three = Movie("The Godfather", 1972, 9.2)

    def test_init_movie(self):
        self.assertEqual('Test', self.movie.name)
        self.assertEqual(2002, self.movie.year)
        self.assertEqual(8.6, self.movie.rating)
        self.assertEqual([], self.movie.actors)
        self.assertEqual(0, len(self.movie.actors))

    def test_movie_name_setter_raises_ex(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ''
        self.assertEqual('Name cannot be an empty string!', str(ex.exception))

    def test_movie_year_setter_raises_ex(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1786
        self.assertEqual('Year is not valid!', str(ex.exception))

    def test_add_actor_to_list_if_not_existing(self):
        self.assertEqual(0, len(self.movie.actors))
        self.movie.add_actor('Ivan')
        self.assertEqual(1, len(self.movie.actors))
        self.assertTrue('Ivan' in self.movie.actors)
        self.movie.add_actor('Stoyan')
        self.assertEqual(2, len(self.movie.actors))
        self.assertTrue('Stoyan' in self.movie.actors)

    def test_adding_existing_actor_returns_error_msg(self):
        self.assertEqual(0, len(self.movie.actors))
        self.movie.add_actor('Ivan')
        self.assertEqual(1, len(self.movie.actors))
        self.assertTrue('Ivan' in self.movie.actors)
        result = self.movie.add_actor('Ivan')
        expected = 'Ivan is already added in the list of actors!'
        self.assertEqual(expected, result)

    def test_gt_returns_correct_answer(self):
        result = self.movie > self.movie_two
        self.assertEqual(f'"{self.movie.name}" is better than "{self.movie_two.name}"', result)
        self.assertEqual(True, self.movie.rating > self.movie_two.rating)
        self.movie_two.rating = 8.9
        result = self.movie < self.movie_two
        self.assertEqual(f'"{self.movie_two.name}" is better than "{self.movie.name}"', result)
        self.assertEqual(True, self.movie.rating < self.movie_two.rating)
        self.movie_two.rating = 8.6
        self.assertEqual(f'"{self.movie_two.name}" is better than "{self.movie.name}"', result)


    def test_repr_returns_correct(self):
        self.movie.add_actor('Ivan')
        self.movie.add_actor('Sotir')
        self.assertEqual(['Ivan', 'Sotir'], self.movie.actors)
        result = str(self.movie)
        expected = f"Name: Test\n" \
                   f"Year of Release: 2002\n" \
                   f"Rating: 8.60\n" \
                   f"Cast: Ivan, Sotir"
        self.assertEqual(expected, result)

    def test_repr_returns_correct_no_list_entry(self):
        result = str(self.movie)
        expected = 'Name: Test\nYear of Release: 2002\nRating: 8.60\nCast: '
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()