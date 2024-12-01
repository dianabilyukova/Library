import unittest
from book import Book

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book(1, "1984", "George Orwell", 1949)

    def test_initialization(self):
        self.assertEqual(self.book.id, 1)
        self.assertEqual(self.book.title, "1984")
        self.assertEqual(self.book.author, "George Orwell")
        self.assertEqual(self.book.year, 1949)
        self.assertEqual(self.book.status, "в наличии")

    def test_to_dict(self):
        expected_dict = {
            "id": 1,
            "title": "1984",
            "author": "George Orwell",
            "year": 1949,
            "status": "в наличии",
        }
        self.assertEqual(self.book.to_dict(), expected_dict)

if __name__ == "__main__":
    unittest.main()

    