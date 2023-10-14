"""Adapterパターンのサンプルプログラム
"""
import abc


class Banner():
    """_summary_
    """

    def __init__(self, string: str) -> None:
        self.__string: str = string

    def show_with_paren(self) -> None:
        """_summary_
        """
        print(f"({self.__string})")

    def show_with_aster(self) -> None:
        """_summary_
        """
        print(f"*{self.__string}*")


class Print(metaclass=abc.ABCMeta):
    """_summary_

    Args:
        metaclass (_type_, optional): _description_. Defaults to abc.ABCMeta.

    Raises:
        NotImplementedError: _description_
        NotImplementedError: _description_
    """
    @abc.abstractmethod
    def print_weak(self) -> None:
        """_summary_
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def print_strong(self) -> None:
        """_summary_
        """
        raise NotImplementedError()


class PrintrBanner(Banner, Print):
    """_summary_

    Args:
        Banner (_type_): _description_
        Print (_type_): _description_
    """

    def print_weak(self):
        super().show_with_paren()

    def print_strong(self):
        super().show_with_aster()


def main():
    """main関数
    """


if __name__ == "__main__":
    main()
