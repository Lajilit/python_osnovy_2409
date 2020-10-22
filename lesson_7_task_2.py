# 2. Реализовать проект расчета суммарного расхода ткани на производство
# одежды. Основная сущность (класс) этого проекта — одежда, которая может
# иметь определенное название. К типам одежды в этом проекте относятся
# пальто и костюм. У этих типов одежды существуют параметры: размер
# (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать
# формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить
# работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные
# на этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, size):
        if isinstance(size, (int, float)):
            self.size = size
        else:
            raise TypeError(f'Invalid argument: must be int or float')

    @property
    def clothes_size(self):
        return self.size

    @clothes_size.setter
    def clothes_size(self, new_size):
        self.__init__(new_size)

    @abstractmethod
    def calc_amount_tissue(self):
        pass


class Coat(Clothes):

    @property
    def calc_amount_tissue(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):

    @property
    def calc_amount_tissue(self):
        return self.size * 2 + 0.3


if __name__ == '__main__':
    a = Coat(6.5)
    b = Suit(8.5)

    print(a.calc_amount_tissue)
    print(b.calc_amount_tissue)
    print(a.size)
    a.size = 8
    print(a.size)
    print(a.calc_amount_tissue)
