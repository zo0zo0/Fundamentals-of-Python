'''
7.3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения
до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
 позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n*****.
'''

from random import random as rnd
from math import ceil

class Cell():

    def __init__(self, quantity):
        self.cell_quantity = round(quantity)
        self.inner_cells = round(rnd() * 100)

    def __add__(self, other): #сложение
        return f"После сложения получилось следующее количество клеток: {round( (self.cell_quantity + other.cell_quantity) / 2)}" \
               f"\nКоличество ячеек у новой клетки = {self.inner_cells + other.inner_cells}"

    def __sub__(self, other): #вычитание
        if (self.inner_cells - other.inner_cells) > 0:
            return f"После вычетания (поглощения) получилось следующее количество клеток: {self.cell_quantity}" \
                    f"\nОднако количество ячеек у новой клетки поубавилось до {self.inner_cells - other.inner_cells}"
        elif (self.inner_cells - other.inner_cells) is None or (self.inner_cells - other.inner_cells) <= 0:
            return f"Количество ячеек недостаточно для процесса 'Вычетания клеток'"

    def __mul__(self): #умножение
        return f"После умножения получилось следующее количество клеток: {round((self.cell_quantity + other.cell_quantity) / 2)}" \
               f"\nКоличество ячеек у новой клетки = {self.inner_cells * other.inner_cells}"

    def __truediv__(self):  #деление
        return f"После деления получилось следующее количество клеток: {round((self.cell_quantity + other.cell_quantity) / 2)}" \
               f"\nКоличество ячеек у новой клетки = {self.inner_cells // other.inner_cells}"

    def make_order(self, qty_in_row):
        rows = ceil(self.inner_cells / qty_in_row)
        balance = self.inner_cells
        printing = ""
        for i in range(rows):
            if balance <= qty_in_row:
                for b in range(self.inner_cells % qty_in_row):
                    printing = printing + "*"
            else:
                for b in range(qty_in_row):
                    printing = printing + "*"
            balance = balance - qty_in_row
            printing = printing + "\n"
        return printing


cell1 = Cell(1)
cell2 = Cell(1)