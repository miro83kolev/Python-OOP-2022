from unittest import TestCase, main

from project.library import Library

class LibraryTest(TestCase):
    def setUp(self) -> None:
        self.library = Library('Library')

    def test_init(self):
        library = Library('Library')

        self.assertEqual('Library', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_library_raises_when_empty_string(self):
        with self.assertRaises(ValueError) as context:
            library = Library('')
        self.assertEqual('Name cannot be empty string!', str(context.exception))

    def test_add_book_adds_author_and_title(self):
        author = 'Author'
        self.library.add_book(author, 'Book1')
        self.library.add_book(author, 'Book2')

        self.assertEqual(1, len(self.library.books_by_authors))
        self.assertTrue(author in self.library.books_by_authors)
        self.assertEqual(['Book1', 'Book2'], self.library.books_by_authors[author])

    def test_add_reader(self):
        reader_name = 'Reader'
        self.library.add_reader(reader_name)

        self.assertEqual(1, len(self.library.readers))
        self.assertTrue(reader_name in self.library.readers)
        self.assertEqual([], self.library.readers[reader_name])

    def test_add_reader_returns_error_message(self):
        reader_name = 'Reader'
        self.library.add_reader(reader_name)
        result = self.library.add_reader(reader_name)

        self.assertEqual(f'{reader_name} is already registered in the {self.library.name} library.', result)

    def test_rent_book_error_message_for_unregistered_reader(self):
        reader_name = 'Reader'
        result = self.library.rent_book(reader_name, 'Author', 'Book1')
        self.assertEqual(f'{reader_name} is not registered in the {self.library.name} Library.', result)

    def test_rent_book_error_message_for_unregistered_author(self):
        reader_name = 'Reader'
        author_name = 'Author'
        self.library.add_reader(reader_name)

        result = self.library.rent_book(reader_name, author_name, 'Book1')
        self.assertEqual(f"{self.library.name} Library does not have any {author_name}'s books.", result)

    def test_rent_book_error_message_for_unregistered_book_title(self):
        reader_name = 'Reader'
        author_name = 'Author'
        book_title = 'Book1'
        self.library.add_reader(reader_name)
        self.library.add_book(author_name, 'random1')

        result = self.library.rent_book(reader_name, author_name, book_title)
        self.assertEqual(f"""{self.library.name} Library does not have {author_name}'s "{book_title}".""", result)

    def test_rent_book_correctly(self):
        reader_name = 'Reader'
        author_name = 'Author'
        book_title = 'Book1'
        book_title_two = 'Book2'
        self.library.add_reader(reader_name)
        self.library.add_book(author_name, book_title)
        self.library.add_book(author_name, book_title_two)

        self.library.rent_book(reader_name, author_name, book_title)
        self.assertEqual([{author_name: book_title}], self.library.readers[reader_name])
        self.assertTrue(book_title not in self.library.books_by_authors[author_name])
        self.assertTrue(book_title_two in self.library.books_by_authors[author_name])
        self.assertEqual(1, len(self.library.books_by_authors[author_name]))


if __name__ == '__main__':
    main()