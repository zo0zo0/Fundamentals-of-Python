'''
7.2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
— одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod

class Send(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def fabrics_calcul(self):
        pass

class Clothes():
    pass

    def __add__(self, other):
        try:
            return f"Общий расход ткани = { round((2 * self.growth + 0.3) + (other.size / 6.5 + 0.5), 2)}"
        except(AttributeError):
            return f"Общий расход ткани = {round((2 * other.growth + 0.3) + (self.size / 6.5 + 0.5), 2)}"

class Suit(Clothes):
    def __init__(self, growth):
        self.growth = growth

    @property
    def fabrics_calcul(self):
        return f"Для пошива костюма вам понадобится : {round(2 * self.growth + 0.3, 2)} м2 ткани"

class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def fabrics_calcul(self):
        return f"Для пошива пальто вам понадобится : {round(self.size / 6.5 + 0.5, 2)} м2 ткани"

s = Suit(75)
c = Coat(55)