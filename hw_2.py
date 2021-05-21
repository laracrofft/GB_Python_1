# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V
# и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property


from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def textile(self):
        pass

    def __init__(self, size, height):
        self.size = size
        self.height = height

    def square_coat(self):
        return self.size / 6.5 + 0.5

    def square_suite(self):
        return self.height * 2 + 0.3

    @property
    def result_square(self):
        return f'Итого площадь ткани составляет: {round((self.size / 6.5 + 0.5) + (self.height * 2 + 0.3), 2)} кв.м.'


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_coat = self.size / 6.5 + 0.5

    def __str__(self):
        return f'Площадь ткани на пальто составляет: {round(self.square_coat, 2)} кв.м.'

    def textile(self):
        pass


class Suite(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_suite = self.height * 2 + 0.3

    def __str__(self):
        return f'Площадь ткани на костюм составляет: {round(self.square_suite, 2)} кв.м.'

    def textile(self):
        pass


coat = Coat(48, 1.8)
suite = Suite(50, 1.6)
print(coat)
print(suite)
print(suite.result_square)
