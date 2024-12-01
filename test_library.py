import unittest
from library import Library
import json
import os

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.test_data_file = "test_data.json"
        self.library = Library(self.test_data_file)

    def tearDown(self):
        # Удаление файла после тестирования
        if os.path.exists(self.test_data_file):
            os.remove(self.test_data_file)

    def test_add_book(self):
        self.library.add_book("1984", "George Orwell", 1949)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "1984")

    def test_remove_book(self):
        self.library.add_book("1984", "George Orwell", 1949)
        result = self.library.remove_book(1)
        self.assertEqual(result, "Книга с ID 1 удалена из библиотеки")
        self.assertEqual(len(self.library.books), 0)

    def test_find_books(self):
        self.library.add_book("1984", "George Orwell", 1949)
        result = self.library.find_books("1984")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "1984")

    def test_update_status(self):
        self.library.add_book("1984", "George Orwell", 1949)
        result = self.library.update_status(1, "выдана")
        self.assertEqual(result, "Статус книги с ID 1 изменен на выдана")
        self.assertEqual(self.library.books[0].status, "выдана")


if __name__ == "__main__":
    unittest.main()

