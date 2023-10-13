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


def main():
    """main関数
    """


if __name__ == "__main__":
    main()
