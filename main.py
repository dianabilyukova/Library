from library import Library
from utils import get_choice, get_user_input


def main():
    """Главная функция"""
    library = Library("data.json")
    while True:
        choice = get_choice()
        if choice == "1":
            title = get_user_input("Введите название книги: ")
            author = get_user_input("Введите автора книги: ")
            year = get_user_input("Введите год издания книги: ")
            library.add_book(title, author, year)

        elif choice == "2":
            book_id = int(get_user_input("Введите ID книги для удаления: "))
            print(library.remove_book(book_id))
        elif choice == "3":
            query = get_user_input("Введите заголовок или автор книги для поиска: ")
            results = library.find_books(query)
            if results:
                for book in results:
                    print(f"ID: {book.id}, Заголовок: {book.title}, "
                          f"Автор: {book.author}, Год: {book.year}, Статус: {book.status}")
                    print("----------------------------------------")
            else:
                print("Книги не найдены")
        elif choice == "4":
            library.display_books()

        elif choice == "5":
            book_id = int(get_user_input("Введите ID книги для обновления статуса: "))
            new_status = get_user_input("Введите новый статус книги (в наличии или выдана): ")
            print(library.update_status(book_id, new_status))


        elif choice == "6":
            print("Выход")
            break
        else:
            print("Неверный ввод")

if __name__ == "__main__":
    main()
