"""Iteratorパターンのサンプルプログラム
"""
import abc


class Iterator(metaclass=abc.ABCmeta):
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


class Aggregate(Iterator, metaclass=abc.ABCmeta):
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

    def __init__(self, name):
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
        self.__books: Book = []
        self.__last: int = 0

    def get_book_at(self, index: int) -> Book:
        """_summary_

        Args:
            index (int): _description_

        Returns:
            Book: _description_
        """
        return self.__books[index]

    def append_book(self, book: Book):
        """_summary_

        Args:
            book (Book): _description_
        """
        self.__books[self.__last] = book
        self.__last += 1

    def get_length(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        return self.__last

    def iterator(self) -> Iterator:
        return BookShelfIterator(BookShelf)


def main():
    """main関数
    """


if __name__ == "__main__":
    main()
