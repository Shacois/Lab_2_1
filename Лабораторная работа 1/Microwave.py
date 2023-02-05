import doctest


class Microwave:
    def __init__(self, timer: int, power: int):
        """
        :param timer: установленное время в секундах
        :param power: максимальная мощность
        Примеры:
        >>> microwave = Microwave(120, 5)
        """
        if not isinstance(timer, (int)):
            raise TypeError
        if timer <= 0:
            raise ValueError
        self.timer = timer

        if not isinstance(power, (int)):
            raise TypeError
        if power < 0:
            raise ValueError
        self.power = power

    def open_microwave(self) -> None:
        """
        Открыть микроволновку
        Примеры:
        >>> microwave = Microwave(120, 5)
        >>> microwave.open_microwave()
        """
        ...

    def close_microwave(self) -> None:
        """
        Закрыть микроволновку
        >>> microwave = Microwave(120, 5)
        >>> microwave.close_microwave()
        """
        ...


    def set_the_time(self, timer: int) -> None:
        """
        Изменение времени
        :return: установленное время
        Примеры:
        >>> microwave = Microwave(120, 5)
        >>> microwave.set_the_time(300)
        """
        if not isinstance(timer, (int)):
            raise TypeError
        if timer <= 0:
            raise ValueError
        ...

    def set_the_power(self, power: int) -> None:
        """
        Изменение мощности
        :raise ValueError: Если установленная мощность превышает максимальную мощность, то возвращается ошибка
        :return: установленная мощность
        Примеры:
        >>> microwave = Microwave(120, 5)
        >>> microwave.set_the_power(4)
        """
        if not isinstance(power, (int)):
            raise TypeError
        if power <= 0:
            raise ValueError
        ...

    def launch(self) -> None:
        """
        Запуск
        Примеры:
        >>> microwave = Microwave(120, 5)
        >>> microwave.launch()
        """
        ...

    def stop(self) -> None:
        """
        Остановка
        Примеры:
        >>> microwave = Microwave(120, 5)
        >>> microwave.stop()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()