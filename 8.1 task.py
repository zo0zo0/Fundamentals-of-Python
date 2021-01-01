'''
8.1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год»
. В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''

import datetime
class Date():

    def __init__(self, fullDate):
        self.fullDate = fullDate

    @classmethod
    def dateExtraction (cls, param):
        extrLst = []
        dateExtr = param.split("-")
        for el in dateExtr:
            extrLst.append(int(el))
        print(extrLst, type(extrLst[0]))

    @staticmethod
    def figureValidation(date):
        timeValidation = date.split("-")
        try:
            New_date = datetime.datetime(int(timeValidation[2]), int(timeValidation[1]), int(timeValidation[0]))
        except ValueError:
            print(f"Date is incorrect {date}")
        else:
            print(f"Date is correct {date}")

d = Date("30-12-2020")