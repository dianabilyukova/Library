def get_choice():
    """Выбор опции из списка"""
    print("\\nВыберите опцию:")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Поиск книг")
    print("4. Отобразить все книги")
    print("5. Обновить статус книги")
    print("6. Выход")
    choice = input("Введите номер опции: ")
    return choice

def get_user_input(prompt: str):
    """Получение ввода пользователя"""
    return input(prompt)


