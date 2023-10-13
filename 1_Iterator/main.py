"""Iteratorパターンのサンプルプログラム
"""
import abc


class IAggregate(metaclass=abc.ABCmeta):
    """_summary_

    Args:
        metaclass (_type_, optional): _description_. Defaults to abc.ABCmeta.
    """
    @abc.abstractmethod
    def iterator(self) -> Iterator:
        """_summary_
        """


class IIterator(metaclass=abc.ABCmeta):
    @abc.abstractmethod
    def has_next(self) -> bool:
        """_summary_
        """

    @abc.abstractmethod
    def next(self) -> object:
        """_summary_
        """


def main():
    """main関数
    """


if __name__ == "__main__":
    main()
