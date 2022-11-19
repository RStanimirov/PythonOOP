from library_project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        # empty list that will store the users (users objects) of the library_project
        self.books_available = {}
        # empty dictionary that will keep information regarding the authors (key: str)
        # and the books available for each of the authors (list of strings)
        self.rented_books = {}
        # empty dictionary that will keep information regarding the usernames (key: str)
        # and nested dictionary as a value which will keep information for the book names (key: str)
        # and days left before returning the book to the library_project -->
        # ({usernames: {book names: days to return}})

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            # if user.username not in self.rented_books:
            #     self.rented_books[user.username] = {}
            # self.rented_books[user.username].update({book_name: days_to_return})
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {book_name: days_to_return}
            else:
                self.rented_books[user.username].update({book_name: days_to_return})
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        else:
            for x in self.rented_books.values():
                for book, days in x.items():
                    if book == book_name:
                        return f'The book "{book_name}" is already rented and will be available in {days} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            self.rented_books[user.username].pop(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"
