from unittest_project.library import Library
import unittest


class Test(unittest.TestCase):
    # def setUp(self) -> None:
    #     pernik_library = Library("Pernik Library")

    def test_init(self):
        pernik_library = Library("Pernik Library")
        self.assertEqual("Pernik Library", pernik_library.name)
        self.assertEqual({}, pernik_library.books_by_authors)
        self.assertEqual({}, pernik_library.readers)

    def test_name_empty_string_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            pernik_library = Library("")
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book(self):
        pernik_library = Library("Pernik Library")
        pernik_library.add_book("Walter Scott", "Ivanhoe")
        pernik_library.add_book("Walter Scott", "Ivanhoe")
        pernik_library.add_book("Walter Scott", "Waverly")
        pernik_library.add_book("Albert Camus", "The Stranger")
        self.assertEqual({'Walter Scott': ['Ivanhoe', 'Waverly'], 'Albert Camus': ['The Stranger']},
                         pernik_library.books_by_authors)
        # self.assertEqual(2, len(pernik_library.books_by_authors))
        # self.assertTrue("Walter Scott" in pernik_library.books_by_authors)
        # self.assertEqual(["Ivanhoe", "Waverly"], pernik_library.books_by_authors["Walter Scott"])

    def test_add_reader_return_text(self):
        pernik_library = Library("Pernik Library")
        pernik_library.add_reader("RS")
        pernik_library.add_reader("Eva")
        self.assertEqual("RS is already registered in the Pernik Library library.",
                         pernik_library.add_reader("RS"))

    def test_add_readers_to_library(self):
        pernik_library = Library("Pernik Library")
        pernik_library.add_reader("RS")
        pernik_library.add_reader("Eva")
        self.assertEqual({'RS': [], 'Eva': []}, pernik_library.readers)
        # self.assertEqual(2, len(pernik_library.readers))
        # self.assertTrue("RS" in pernik_library.readers)
        # self.assertEqual([], pernik_library.readers["RS"])

    def test_rent_book_successful(self):
        pernik_library = Library("Pernik Library")
        pernik_library.add_book("Walter Scott", "Ivanhoe")
        pernik_library.add_book("Walter Scott", "Waverly")
        pernik_library.add_book("Albert Camus", "The Stranger")
        pernik_library.add_reader("RS")
        pernik_library.add_reader("Eva")
        self.assertEqual({'RS': [], 'Eva': []}, pernik_library.readers)
        pernik_library.rent_book("RS", "Walter Scott", "Ivanhoe")
        self.assertEqual({'RS': [{'Walter Scott': 'Ivanhoe'}], 'Eva': []}, pernik_library.readers)
        # book_title_index = pernik_library.books_by_authors["Walter Scott"].index("Ivanhoe")
        # self.assertEqual([{"Walter Scott": "Ivanhoe"}], pernik_library.readers["RS"])
        # self.assertEqual(1, len(pernik_library.books_by_authors["Walter Scott"]))
        self.assertEqual({'Walter Scott': ['Waverly'], 'Albert Camus': ['The Stranger']},
                         pernik_library.books_by_authors)
        # self.assertTrue("Ivanhoe" not in pernik_library.books_by_authors["Walter Scott"])
        # self.assertTrue("Waverly" in pernik_library.books_by_authors["Walter Scott"])

    def test_rent_book_if_reader_not_in_readers(self):
        pernik_library = Library("Pernik Library")
        pernik_library.add_book("Walter Scott", "Ivanhoe")
        pernik_library.add_book("Walter Scott", "Waverly")
        pernik_library.add_book("Albert Camus", "The Stranger")
        pernik_library.add_reader("RS")
        pernik_library.add_reader("Eva")
        self.assertEqual("John is not registered in the Pernik Library Library.",
                         pernik_library.rent_book("John", "Walter Scott", "Waverly"))

    def test_rent_book_if_book_author_not_in_books(self):
        pernik_library = Library("Pernik Library")
        pernik_library.add_book("Walter Scott", "Ivanhoe")
        pernik_library.add_book("Walter Scott", "Waverly")
        pernik_library.add_book("Albert Camus", "The Stranger")
        pernik_library.add_reader("RS")
        pernik_library.add_reader("Eva")
        self.assertEqual("Pernik Library Library does not have any Astrid Lindgren's books.",
                         pernik_library.rent_book("Eva", "Astrid Lindgren", "Pippi Longsocks"))

    def test_rent_book_if_book_title_not_in_books(self):
        pernik_library = Library("Pernik Library")
        pernik_library.add_book("Walter Scott", "Ivanhoe")
        pernik_library.add_book("Walter Scott", "Waverly")
        pernik_library.add_book("Albert Camus", "The Stranger")
        pernik_library.add_reader("RS")
        pernik_library.add_reader("Eva")
        self.assertEqual("""Pernik Library Library does not have Walter Scott's "Rob Roy".""",
                         pernik_library.rent_book("RS", "Walter Scott", "Rob Roy"))


if __name__ == '__main__':
    unittest.main()
