# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Car:
    def __init__(self, make: str, model: str, year: int):
        """
        Создание и подготовка к работе объекта "Машина"

        :param make: Производитель машины
        :param model: Модель машины
        :param year: Год выпуска машины

        Примеры:
        >>> car = Car("Toyota", "Corolla", 2020)
        """
        if not isinstance(make, str):
            raise TypeError("Производитель должен быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not isinstance(year, int) or year < 1886:
            raise ValueError("Год выпуска должен быть целым числом, не меньше 1886")

        self.make = make
        self.model = model
        self.year = year

        def start_engine(self) -> None:
            """
            Время запуска двигателя
            """
            ...

        def drive(self, distance: float) -> None:
            """
            Движение машины на заданное расстояние.

            :param distance: Расстояние, которое должна проехать машина в километрах

            Примеры:
            >>> car = Car("Toyota", "Corolla", 2020)
            >>> car.drive(10.5)  # Пример использования
            """
            ...


class Book:
    def __init__(self, title: str, author: str, num_pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param num_pages: Количество страниц в книге

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        """
        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        if not isinstance(num_pages, int) or num_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        self.title = title
        self.author = author
        self.num_pages = num_pages

    def read(self, pages: int) -> None:
        """
        Чтение определенного количества страниц из книги.

        :param pages: Количество страниц для чтения

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.read(20)  # Пример использования
        """
        ...

    def bookmark_page(self, page: int) -> None:
        """
        Закладка на определенной странице.

        :param page: Номер страницы для закладки

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.bookmark_page(100)  # Пример использования
        """
        ...

class SocialNetwork:
    def __init__(self, name: str, max_users: int):
        """
        Создание и подготовка к работе объекта "Социальная сеть"

        :param name: Название социальной сети
        :param max_users: Максимальное количество пользователей

        Примеры:
        >>> network = SocialNetwork("MyNetwork", 1000)
        """
        if not isinstance(name, str):
            raise TypeError("Название социальной сети должно быть строкой")
        if not isinstance(max_users, int) or max_users <= 0:
            raise ValueError("Максимальное количество пользователей должно быть положительным целым числом")

        self.name = name
        self.max_users = max_users

    def register_user(self, username: str) -> None:
        """
        Регистрация нового пользователя.

        :param username: Имя пользователя

        Примеры:
        >>> network = SocialNetwork("MyNetwork", 1000)
        >>> network.register_user("Alice")  # Пример использования
        """
        ...

    def delete_account(self, username: str) -> None:
        """
        Удаление аккаунта пользователя.

        :param username: Имя пользователя

        Примеры:
        >>> network = SocialNetwork("MyNetwork", 1000)
        >>> network.delete_account("Alice")  # Пример использования
        """
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
