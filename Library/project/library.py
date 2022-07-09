class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author, book_name, days_to_return, user):
        # if author is part of book_available and book_name for this author is available
        if author in self.books_available and book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            return f'{book_name} successfully rented for the next {days_to_return} days!'

        for user_books in self.rented_books.values():
            if book_name in user_books:
                return f'The book "{book_name}" is already rented and will be available in {user_books[book_name]} days!'


    def return_book(self, author, book_name, user):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        self.rented_books[user.username].pop(book_name)






