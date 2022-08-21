from project.library import Library

from unittest import TestCase, main


class LibraryTest(TestCase):
    def setUp(self) -> None:
        self.library = Library('Test')

    def test_init_library(self):
        self.assertEqual('Test', self.library.name)
        self.assertDictEqual({}, self.library.books_by_authors)
        self.assertDictEqual({}, self.library.readers)

    def test_if_empty_name_raises_ex(self):
        with self.assertRaises(ValueError) as ex:
            self.library.name = ''
        self.assertEqual('Name cannot be empty string!', str(ex.exception))

    def test_add_book_if_author_not_in_books(self):
        self.library.add_book('A', 'Title')
        self.assertTrue("A" in self.library.books_by_authors)
        self.assertDictEqual({'A': ['Title']}, self.library.books_by_authors)
        self.assertEqual(1, len(self.library.books_by_authors))
        self.library.add_book('B', 'Title')
        self.assertTrue("B" in self.library.books_by_authors)
        self.assertDictEqual({'A': ['Title'],'B': ['Title']}, self.library.books_by_authors)
        self.assertEqual(2, len(self.library.books_by_authors))

    def test_add_book_if_title_does_not_exist(self):
        self.library.add_book('A', 'Title')
        self.assertTrue("A" in self.library.books_by_authors)
        self.assertDictEqual({'A': ['Title']}, self.library.books_by_authors)
        self.assertEqual(1, len(self.library.books_by_authors))
        self.library.add_book('A', 'New')
        self.assertTrue('New' in self.library.books_by_authors['A'])
        self.assertDictEqual({'A': ['Title', 'New']}, self.library.books_by_authors)
        self.assertEqual(2, len(self.library.books_by_authors['A']))

    def test_add_book_if_title_exists(self):
        self.library.add_book('A', 'Title')
        self.assertTrue("A" in self.library.books_by_authors)
        self.assertTrue('Title' in self.library.books_by_authors['A'])
        self.assertEqual(1, len(self.library.books_by_authors['A']))
        self.library.add_book('A', 'Title')
        self.assertEqual(1, len(self.library.books_by_authors['A']))

    def test_add_reader_whom_does_not_exist(self):
        self.library.add_reader('Peter')
        self.assertTrue('Peter' in self.library.readers)
        self.assertEqual(1, len(self.library.readers))
        self.assertDictEqual({'Peter': []}, self.library.readers)

    def test_add_book_returns_correctly_str(self):
        self.library.readers['John'] = []
        result = self.library.add_reader("John")
        self.assertEqual("John is already registered in the Test library.", result)

    def test_rent_book_when_reader_does_not_exist(self):
        result = self.library.rent_book('John', 'A', 'book')
        expected = 'John is not registered in the Test Library.'
        self.assertEqual(expected, result)
        self.assertTrue('John' not in self.library.readers)

    def test_rent_book_when_author_does_not_exist(self):
        self.library.readers['John'] = []
        result = self.library.rent_book('John', 'A', 'book')
        expected = "Test Library does not have any A's books."
        self.assertEqual(expected, result)
        self.assertDictEqual({}, self.library.books_by_authors)
        self.assertTrue('A' not in self.library.books_by_authors)

    def test_when_title_does_not_exists(self):
        self.library.add_reader('John')
        self.library.books_by_authors['A'] = 'Me'
        result = self.library.rent_book('John', 'A', 'new')
        expected = """Test Library does not have A's "new"."""
        self.assertEqual(expected, result)
        self.assertTrue('New' not in self.library.books_by_authors['A'])

    def test_rent_a_book_adds_to_readers_list(self):
        self.library.add_reader('John')
        self.library.add_book('A', 'book')
        self.library.rent_book("John", "A", "book")
        self.assertEqual({'John': [{'A': 'book'}]}, self.library.readers)
        self.assertTrue('John' in self.library.readers)
        self.assertTrue('A' in self.library.books_by_authors)

    def test_rent_book_removes_title_from_authors_books_list(self):
        self.library.add_reader('John')
        self.library.add_book("A", "book 1")
        self.library.add_book('A', 'book2')
        self.assertEqual(2, len(self.library.books_by_authors['A']))
        self.library.rent_book('John', 'A', 'book2')
        self.assertEqual(1, len(self.library.books_by_authors['A']))
        self.assertTrue('book2' not in self.library.books_by_authors['A'])


if __name__ == '__main__':
    main()
