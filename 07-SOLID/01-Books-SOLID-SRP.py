class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self):
        pass

    def find_book(self, title):
        try:
            return [x for x in self.books if x.title == title][0]
        except IndexError:
            return "Book not found"

    def __str__(self):
        return f"{book.title} by {book.author}"


library = Library()

for i in range(1, 21):
    book = Book(f"'Title {i}'", f"Author {i}")
    library.add_book(book)
    print(library)
