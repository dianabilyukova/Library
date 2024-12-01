import json
from book import Book

class Library:
    def __init__(self, data_file: str):
        self.data_file = data_file
        self.books = []
        self.load_books()

    def load_books(self):
        """Загрузка книг из файла"""
        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.books = [Book(**book) for book in data]
        except FileNotFoundError:
            self.books = []

    def save_books(self):
        """Сохранение книг в файл"""
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False)

    def add_book(self, title: str, author: str, year: int):
        """Добавление книги в библиотеку"""
        new_id = len(self.books) + 1
        book = Book(new_id, title, author, year, status = "в наличии")
        self.books.append(book)
        self.save_books()
        print(f"Книга '{title}' добавлена в библиотеку. ID: {new_id}, Статус: в наличии")

    def remove_book(self, book_id: int):
        """Удаление книги из библиотеки"""
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                return f"Книга с ID {book_id} удалена из библиотеки"
        return f'Книга с ID {book_id} не найдена'

    def find_books(self, query: str):
        """Поиск книг в библиотеке по заголовку, автору или году"""
        result = [
            book for book in self.books
            if (query.lower() in book.title.lower() or
               query.lower() in book.author.lower() or
               query == str(book.year))
        ]
        return result

    def display_books(self):
        """Отображение списка книг в библиотеке"""
        if not self.books:
            print("Библиотека пуста")
            return
        for book in self.books:
            print(f"ID: {book.id}, Заголовок: {book.title}, "
                  f"Автор: {book.author}, Год: {book.year}, Статус: {book.status}")
            print("----------------------------------------")

    def update_status(self, book_id: int, new_status: str):
        """Обновление статуса книги в библиотеке"""
        for book in self.books:
            if book.id == book_id:
                if new_status in ["в наличии", "выдана"]:
                    book.status = new_status
                    self.save_books()
                    return f"Статус книги с ID {book_id} изменен на {new_status}"
                return f"Недопустимый статус. Возможные варианты: в наличии или выдана"
        return f"Книга с ID {book_id} не найдена"




