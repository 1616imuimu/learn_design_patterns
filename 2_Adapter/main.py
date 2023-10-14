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


def main():
    """main関数
    """


if __name__ == "__main__":
    main()
