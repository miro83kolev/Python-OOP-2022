from project.library import Library

from unittest import TestCase, main

class LibraryTests(TestCase):
    def test_init_library(self):
        library = Library('Test')
        self.assertEqual('Test', library.name)
        self.assertDictEqual({}, library.books_by_authors)
        self.assertDictEqual({}, library.readers)

    def test_name_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            library = Library('')
        self.assertEqual('Name cannot be empty string!', str(context.exception))

    def test_add_book(self):
        library = Library('Test')
        library.add_book('Author', 'Book1')
        library.add_book('Author', 'Book2')
        self.assertEqual(1, len(library.books_by_authors))
        self.assertTrue('Author' in library.books_by_authors)
        self.assertEqual(['Book1', 'Book2'], library.books_by_authors['Author'])

    def test_add_reader(self):
        library = Library('Test')
        reader_name = 'Pesho'
        library.add_reader(reader_name)
        self.assertEqual(1, len(library.readers))
        self.assertTrue(reader_name in library.readers)
        self.assertEqual([], library.readers[reader_name])

    def test_add_reader_when_existing(self):
        library = Library('Test')
        reader_name = 'Pesho'
        library.add_reader(reader_name)
        result = library.add_reader(reader_name)
        self.assertEqual(f'{reader_name} is already registered in the {library.name} library.', result)

    def test_rent_book_reader_not_registered_raises_error_message(self):
        library = Library('Test')
        result = library.rent_book('reader', 'author', 'book1')
        self.assertEqual(f'reader is not registered in the {library.name} Library.', result)

    def test_rent_book_author_not_registered_raises_error_message(self):
        library = Library('Test')
        library.add_reader('reader')
        result = library.rent_book('reader', 'author', 'book1')
        self.assertEqual(f'{library.name} Library does not have any author\'s books.', result)

    def test_rent_book_title_not_registered_raises_error_message(self):
        library = Library('Test')
        reader = 'Pesho'
        author = 'Gosho'
        title = 'title'
        library.add_reader(reader)
        library.add_book(author, 'another')
        result = library.rent_book(reader, author, title)
        self.assertEqual(f"""{library.name} Library does not have {author}'s "{title}".""", result)

    def test_rent_books_correctly(self):
        library = Library('Test')
        reader = 'Pesho'
        author = 'Gosho'
        title = 'title'
        second_title = 'title2'
        library.add_reader(reader)
        library.add_book(author, title)
        library.add_book(author, second_title)
        library.rent_book(reader, author, title)
        self.assertEqual([{author: title}], library.readers[reader])
        self.assertTrue(title not in library.books_by_authors[author])
        self.assertTrue(second_title in library.books_by_authors[author])
        self.assertEqual(1, len(library.books_by_authors[author]))



















if __name__ == '__main__':
    main()