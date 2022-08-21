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


















if __name__ == '__main__':
    main()
