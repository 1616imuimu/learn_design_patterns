"""Adapterパターンのサンプルプログラム
"""


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


class Print():
    """_summary_
    """

    def print_weak(self) -> None:
        """_summary_
        """

    def print_strong(self) -> None:
        """_summary_
        """


class PrintrBanner(Print):
    """_summary_

    Args:
        Print (_type_): _description_
    """

    def __init__(self, string: str) -> None:
        self.__banner: Banner = Banner(string)

    def print_weak(self):
        self.__banner.show_with_paren()

    def print_strong(self):
        self.__banner.show_with_aster()


def main():
    """main関数
    """
    p: Print = PrintrBanner("Hello")
    p.print_weak()
    p.print_strong()


if __name__ == "__main__":
    main()
