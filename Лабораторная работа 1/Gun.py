import doctest


class Gun:
    def __init__(self, maximum_ammo: int, left_shots_in_clip: int):
        """
        :param maximum_ammo: Вместимость магазина
        :param left_shots_in_clip: Патронов в магазине
        Примеры:
        >>> revolver = Gun(6, 6)
        """
        if not isinstance(maximum_ammo, (int)):
            raise TypeError
        if maximum_ammo <= 0:
            raise ValueError
        self.maximum_ammo = maximum_ammo

        if not isinstance(left_shots_in_clip, (int)):
            raise TypeError
        if left_shots_in_clip < 0:
            raise ValueError
        self.left_shots_in_clip = left_shots_in_clip

    def is_empty_gun(self) -> bool:
        """
        Функция которая проверяет является ли магазин пустым
        :return: Является ли магазин пустым
        Примеры:
        >>> revolver = Gun(6, 6)
        >>> revolver.is_empty_gun()
        """
        ...

    def reload(self, ammo: int) -> None:
        """
        Переазярадка
        :param ammo: Количество добавляемых патронов
        :raise ValueError: Если количество добавляемых патронов превышает свободное место в магазине, то вызываем ошибку
        Примеры:
        >>> revolver = Gun(6, 5)
        >>> revolver.reload(1)
        """
        if not isinstance(ammo, (int)):
            raise TypeError
        if ammo < 0:
            raise ValueError
        ...

    def shoot(self, number_of_shots: int) -> None:
        """
        Выстрел
        :param number_of_shots: количество выстрелов
        :raise ValueError: Если количество выстрелов превышает количество воды в стакане,
        то возвращается ошибка.
        :return: Количество патронов, оставшихся после выстрела
        Примеры:
        >>> revolver = Gun(6, 6)
        >>> revolver.shoot(6)
        """
        if not isinstance(number_of_shots, (int)):
            raise TypeError
        if number_of_shots < 0:
            raise ValueError
        ...


if __name__ == "__main__":
    doctest.testmod()