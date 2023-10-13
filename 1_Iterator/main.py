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


def main():
    """main関数
    """


if __name__ == "__main__":
    main()
