from project.bookstore import Bookstore

from unittest import TestCase, main

class BookstoreTests(TestCase):
    def setUp(self):
        self.bookstore = Bookstore(2)

    def test_init_bookstore(self):
        self.assertEqual(2, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)
        # test the private attr
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)

    def test_book_limit_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.bookstore.books_limit = 0
        self.assertEqual('Books limit of 0 is not valid', str(ex.exception))

    def test_book_limit_zero_raises_when_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.bookstore.books_limit = -1
        self.assertEqual('Books limit of -1 is not valid', str(ex.exception))

    def test_len_returns_correctly(self):
        result = len(self.bookstore)
        expected = 0
        self.assertEqual(expected, result)

        self.bookstore.books_limit = 5
        self.bookstore.receive_book('Book', 2)
        self.bookstore.receive_book('Book_one', 2)
        result = len(self.bookstore)
        expected = 4
        self.assertEqual(expected, result)

    def test_receive_book_not_enough_space(self):
        self.bookstore.books_limit = 3
        self.bookstore.receive_book('Book', 2)
        self.bookstore.receive_book('Book_one', 1)
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('Book3', 1)
        self.assertEqual('Books limit is reached. Cannot receive more books!', str(ex.exception))

    def test_receive_when_title_does_not_exist(self):
        self.bookstore.books_limit = 3
        self.bookstore.receive_book('Book', 1)
        self.bookstore.receive_book('Book2', 1)
        self.assertEqual(2, len(self.bookstore))

        result = self.bookstore.receive_book('Book3', 1)
        self.assertEqual({'Book': 1, 'Book2': 1, 'Book3': 1}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual('1 copies of Book3 are available in the bookstore.', result)

    def test_receive_when_title_exists(self):
        self.bookstore.books_limit = 3
        self.bookstore.receive_book('Book', 1)
        self.assertTrue('Book' in self.bookstore.availability_in_store_by_book_titles)
        self.assertTrue(1, len(self.bookstore.availability_in_store_by_book_titles))
        result = self.bookstore.receive_book('Book', 2)
        self.assertTrue(3, len(self.bookstore.availability_in_store_by_book_titles))
        self.assertEqual("3 copies of Book are available in the bookstore.", result)

    def test_sell_book_when_book_does_not_exist(self):
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('Book', 1)
        self.assertEqual('Book Book doesn\'t exist!', str(ex.exception))

    def test_sell_when_not_enough_copies(self):
        self.bookstore.books_limit = 3
        self.bookstore.receive_book('Book', 1)
        self.bookstore.receive_book('Book2', 1)
        self.assertEqual({'Book': 1, 'Book2': 1}, self.bookstore.availability_in_store_by_book_titles)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('Book', 2)
        self.assertEqual('Book has not enough copies to sell. Left: 1', str(ex.exception))
        self.assertEqual({'Book': 1, 'Book2': 1}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_when_enough_copies(self):
        self.bookstore.books_limit = 5
        self.bookstore.receive_book('Book', 3)
        self.bookstore.receive_book('Book2', 2)
        result = self.bookstore.sell_book('Book', 2)
        self.assertEqual({'Book': 1, 'Book2': 2}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual('Sold 2 copies of Book', result)
        self.assertEqual(2, self.bookstore.total_sold_books)
        self.assertEqual(2, self.bookstore._Bookstore__total_sold_books)

    def test_string_returns_correct(self):
        self.bookstore.books_limit = 5
        self.bookstore.receive_book('Book', 2)
        self.bookstore.receive_book('Book2', 2)
        self.bookstore.sell_book('Book', 1)
        result = str(self.bookstore)
        expected = "Total sold books: 1\nCurrent availability: 3\n - Book: 1 copies\n - Book2: 2 copies"
        self.assertEqual(expected, result)

    def test_string_method_if_not_books(self):
        bookstore = Bookstore(3)
        result = str(bookstore)
        expected = "Total sold books: 0\nCurrent availability: 0"
        self.assertEqual(expected, result)

    def test_total_sold_books_returns_correct_number(self):
        bookstore = Bookstore(4)
        bookstore.receive_book("Book", 3)
        bookstore.receive_book("Book2", 1)

        result = bookstore.sell_book("Book", 2)
        self.assertEqual({"Book": 1, "Book2": 1}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(f"Sold 2 copies of Book", result)
        self.assertEqual(2, bookstore.total_sold_books)
        self.assertEqual(2, bookstore._Bookstore__total_sold_books)

        result = bookstore.sell_book("Book", 1)
        self.assertEqual({"Book": 0, "Book2": 1}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(f"Sold 1 copies of Book", result)
        self.assertEqual(3, bookstore.total_sold_books)
        self.assertEqual(3, bookstore._Bookstore__total_sold_books)
























if __name__ == '__main__':
    main()
