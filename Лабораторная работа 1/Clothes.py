import doctest


class Clothes:
    def __init__(self, size: int):
        """
        :param size: размер одежды
        Примеры:
        >>> cap = Clothes(12)
        """
        if not isinstance(size, (int)):
            raise TypeError
        if size <= 0:
            raise ValueError
        self.size = size

    def put_on_clothes(self) -> None:
        """
        Надеть одежду
        Примеры:
        >>> cap = Clothes(12)
        >>> cap.put_on_clothes()
        """
        ...

    def remove_clothes(self) -> None:
        """
        Снять одежду
        Примеры:
        >>> cap = Clothes(12)
        >>> cap.remove_clothes()
        """
        ...

    def wash_clothes(self) -> None:
        """
        Постирать одежду
        Примеры:
        >>> cap = Clothes(12)
        >>> cap.wash_clothes()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()