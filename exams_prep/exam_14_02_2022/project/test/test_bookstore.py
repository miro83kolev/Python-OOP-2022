from project.bookstore import Bookstore

from unittest import TestCase, main


class BookstoreTests(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(10)

    def test_init_bookstore(self):
        bookstore = Bookstore(10)
        self.assertEqual(10, bookstore.books_limit)
        self.assertDictEqual({}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, bookstore.total_sold_books)

    def test_property_total_sold_books(self):
        self.total_sold_books = 0
        self.assertEqual(0, self.total_sold_books)
        self.bookstore.receive_book('Book', 5)
        self.bookstore.sell_book('Book', 2)
        self.total_sold_books = 2
        self.assertEqual(2, self.total_sold_books)

    def test_property_total_books_limit(self):
        self.bookstore.books_limit = 10
        self.assertEqual(10, self.bookstore.books_limit)
        self.bookstore.books_limit = 20
        self.assertEqual(20, self.bookstore.books_limit)

    def test_books_limit_raises_exception(self):
        with self.assertRaises(ValueError) as ex:
            bookstore = Bookstore(-1)
        self.assertEqual("Books limit of -1 is not valid", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            bookstore = Bookstore(0)
        self.assertEqual("Books limit of 0 is not valid", str(ex.exception))

    def test_len_method_returns_correctly(self):
        book1 = self.bookstore.receive_book('Title', 3)
        book2 = self.bookstore.receive_book('Mine', 2)
        result = len(self.bookstore)
        self.assertEqual(5, result)
        self.bookstore.sell_book("Title", 2)
        result = len(self.bookstore)
        self.assertEqual(3, result)
        self.bookstore.receive_book('New', 1)
        final_result = len(self.bookstore)
        self.assertEqual(4, final_result)
        self.assertEqual({'Mine': 2, 'New': 1, 'Title': 1}, self.bookstore.availability_in_store_by_book_titles)

    def test_len_method_initial(self):
        expected = self.bookstore.__len__()
        self.assertEqual(expected, 0)

    def test_receive_book_raises_exception_if_less_space_then_books(self):
        bookstore = Bookstore(1)
        with self.assertRaises(Exception) as context:
            for index in range(5):
                self.bookstore.receive_book('Title', 5)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(context.exception))

    def test_receive_if_book_not_in_bookstore(self):
        self.bookstore.availability_in_store_by_book_titles['Title'] = 1
        self.assertEqual(1, len(self.bookstore.availability_in_store_by_book_titles))
        self.assertTrue('Title' in self.bookstore.availability_in_store_by_book_titles)

    def test_receive_book_returns_proper_message(self):
        result = self.bookstore.receive_book('Title', 4)
        expected = "4 copies of Title are available in the bookstore."
        self.assertEqual(expected, result)

    def test_receive_book_adds_correctly_to_dicts(self):
        self.bookstore.receive_book('Title', 3)
        self.bookstore.receive_book('Mine', 4)
        self.assertEqual({"Title": 3, "Mine": 4}, self.bookstore.availability_in_store_by_book_titles)
        self.bookstore.receive_book('Title', 3)
        self.assertEqual({"Title": 6, "Mine": 4}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_raises_error_if_book_not_in_the_list(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('Title', 3)
        self.assertEqual('Book Title doesn\'t exist!', str(ex.exception))

    def test_number_of_books_to_sell_more_than_available_raises_exception(self):
        self.bookstore.availability_in_store_by_book_titles['Title'] = 1
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('Title', 2)
        self.assertEqual("Title has not enough copies to sell. Left: 1", str(ex.exception))

    def test_number_to_sell_less_than_available(self):
        self.bookstore.availability_in_store_by_book_titles['Title'] = 5
        result = self.bookstore.sell_book('Title', 1)
        self.assertEqual('Sold 1 copies of Title', result)
        self.assertEqual(4, self.bookstore.availability_in_store_by_book_titles['Title'])
        new_result = self.bookstore.sell_book('Title', 2)
        self.assertEqual('Sold 2 copies of Title', new_result)
        self.assertEqual(2, self.bookstore.availability_in_store_by_book_titles['Title'])

    def test_str_returns_proper_output(self):
        self.bookstore.receive_book('Book', 5)
        self.bookstore.sell_book('Book', 2)
        actual = str(self.bookstore)
        expected = "Total sold books: 2\nCurrent availability: 3\n - Book: 3 copies"
        self.assertEqual(actual, expected)

    def test_limit_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.bookstore.books_limit = 0
        self.assertEqual(str(ex.exception), "Books limit of 0 is not valid")

    def test_receive_book_correct_message(self):
        expected = self.bookstore.receive_book('Book', 1)
        self.assertEqual(expected, "1 copies of Book are available in the bookstore.")

    def test_receive_book_raises(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('Book', 12)
        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")

    def test_sell_book_correct_message(self):
        expected = self.bookstore.sell_book('Book', 1)
        self.assertEqual(expected, "Sold 1 copies of Book")


if __name__ == '__main__':
    main()
