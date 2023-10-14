"""Iteratorパターンのサンプルプログラム
"""
import abc
from typing import cast


class Iterator(metaclass=abc.ABCMeta):
    """_summary_

    Args:
        metaclass (_type_, optional): _description_. Defaults to abc.ABCmeta.

    Raises:
        NotImplementedError: _description_
        NotImplementedError: _description_
    """
    @abc.abstractmethod
    def has_next(self) -> bool:
        """_summary_
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def next(self) -> object:
        """_summary_
        """
        raise NotImplementedError()


class Aggregate(metaclass=abc.ABCMeta):
    """_summary_

    Args:
        metaclass (_type_, optional): _description_. Defaults to abc.ABCmeta.
    """
    @abc.abstractmethod
    def iterator(self) -> Iterator:
        """_summary_
        """
        raise NotImplementedError()


class Book():
    """_summary_
    """

    def __init__(self, name: str) -> None:
        self.__name: str = name

    def get_name(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return self.__name


class BookShelf(Aggregate):
    """_summary_

    Args:
        Aggregate (_type_): _description_
    """

    def __init__(self):
        self.__books: list[Book] = []
        self.__last: int = 0

    def get_book_at(self, index: int) -> Book:
        """_summary_

        Args:
            index (int): _description_

        Returns:
            Book: _description_
        """
        return self.__books[index]

    def append_book(self, book: Book) -> None:
        """_summary_

        Args:
            book (Book): _description_
        """
        self.__books.append(book)
        self.__last += 1

    def get_length(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        return self.__last

    def iterator(self) -> Iterator:
        return BookShelfIterator(self)


class BookShelfIterator(Iterator):
    """_summary_

    Args:
        Iterator (_type_): _description_
    """

    def __init__(self, book_shelf: BookShelf):
        self.__book_shelf: BookShelf = book_shelf
        self.__index: int = 0

    def has_next(self) -> bool:
        if self.__index < self.__book_shelf.get_length():
            return True
        else:
            return False

    def next(self) -> object:
        book: Book = self.__book_shelf.get_book_at(self.__index)
        self.__index += 1
        return book


def main():
    """main関数
    """
    book_shelf: BookShelf = BookShelf()
    book_shelf.append_book(Book("Around the World in 80 Days"))
    book_shelf.append_book(Book("Bible"))
    book_shelf.append_book(Book("Cinderella"))
    book_shelf.append_book(Book("Daddy-Long-Legs"))

    it: Iterator = book_shelf.iterator()
    while it.has_next():
        book: Book = cast(Book, it.next())
        print(book.get_name())


if __name__ == "__main__":
    main()
