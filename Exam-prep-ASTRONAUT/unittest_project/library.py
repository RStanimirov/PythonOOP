class Library:
    def __init__(self, name):
        self.name = name
        self.books_by_authors = {}
        self.readers = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Name cannot be empty string!")
        self.__name = value

    def add_book(self, author, title):
        if author not in self.books_by_authors:
            self.books_by_authors[author] = []
        if title not in self.books_by_authors[author]:
            self.books_by_authors[author].append(title)

    def add_reader(self, name):
        if name not in self.readers:
            self.readers[name] = []
        else:
            return f"{name} is already registered in the {self.name} library."

    def rent_book(self, reader_name, book_author, book_title):
        if reader_name not in self.readers:
            return f"{reader_name} is not registered in the {self.name} Library."
        if book_author not in self.books_by_authors:
            return f"{self.name} Library does not have any {book_author}'s books."
        if book_title not in self.books_by_authors[book_author]:
            return f"""{self.name} Library does not have {book_author}'s "{book_title}"."""
        self.readers[reader_name].append({book_author: book_title})
        book_title_index = self.books_by_authors[book_author].index(book_title)
        del self.books_by_authors[book_author][book_title_index]


# pernik_library = Library("Pernik Library")
# pernik_library.add_book("Walter Scott", "Ivanhoe")
# pernik_library.add_book("Walter Scott", "Waverly")
# pernik_library.add_book("Albert Camus", "The Stranger")
# # pernik_library.add_book("Gwyn Thomas", "All Things Betray Thee")
# # pernik_library.add_book("J. Sallinger", "Catcher In The Rye")
# # pernik_library.add_book("Jack London", "Martin Eden")
# # pernik_library.add_book("Herman Melville", "Moby Dick")
#
# print(pernik_library.books_by_authors)
#
# pernik_library.add_reader("RS")
# pernik_library.add_reader("Eva")
# pernik_library.rent_book("RS", "Walter Scott", "Ivanhoe")
#
# print(pernik_library.readers)
# print(pernik_library.books_by_authors)