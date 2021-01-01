'''
8.7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''

class Complex_figure():
    def __init__(self, first, second):
        self.figure = complex(first, second)

    def __add__(self, other):
        return f"Сложение комплексных чисел:\n" \
               f"{self.figure + other.figure}"

    def __mul__(self, other):
        return f"Умножение комплексных чисел:\n" \
               f"{self.figure * other.figure}"

comp_f1 = Complex_figure(1, 2)
comp_f2 = Complex_figure(2, 3)