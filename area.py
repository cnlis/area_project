import math
import operator
from abc import abstractmethod, ABC
from functools import reduce


class _AbstractFigure(ABC):

    _sides : list[float]
    _cached_area : float | None = None
    _name : str | None = None

    @abstractmethod
    def _calc_area(self) -> float:
        ...

    def get_area(self) -> float:
        if self._cached_area is None:
            self._cached_area = self._calc_area()
        return self._cached_area

    def __init__(self, *sides : float):
        self._sides = list(sides)
        if min(self._sides) < 0:
            raise Exception('Сторона фигуры не может быть отрицательной')

    def __str__(self) -> str:
        return self._name


class _Circle(_AbstractFigure):

    def _calc_area(self) -> float:
        return math.pi * self._sides.pop()**2

    def __init__(self, *sides: float):
        super().__init__(*sides)
        self._name = 'круг'


class _Triangle(_AbstractFigure):

    def _calc_area(self) -> float:
        half_p = sum(self._sides) / 2
        return math.sqrt(half_p * reduce(
            operator.mul, (half_p - x for x in self._sides), 1))

    def __init__(self, *sides: float):
        super().__init__(*sides)
        self._sides.sort()
        if sum(self._sides) > 0 and self._sides[2] >= sum(self._sides[:2]):
            raise Exception('Длина одной из сторон больше суммы других '
                            'сторон. Такой треугольник не существует')
        is_right = self._sides[0]**2 + self._sides[1]**2 == self._sides[2]**2
        self._name = f'{"прямоугольный " if is_right else ""}треугольник'


class Figure:

    def __new__(cls, *sides: float) -> _AbstractFigure:
        match len(sides):
            case 0: raise Exception('У фигуры должна быть как '
                                    'минимум одна сторона')
            case 1: return _Circle(*sides)
            case 2: raise Exception('Фигуры с двумя сторонами не существует')
            case 3: return _Triangle(*sides)
            case _: raise Exception('Фигуры с количеством сторон больше, '
                                    'чем 3 на данный момент не поддерживаются')


if __name__ == '__main__':
    print('Модуль реализует класс Figure, параметрами конструктора которого '
          'являются стороны треугольника или радиус круга')

