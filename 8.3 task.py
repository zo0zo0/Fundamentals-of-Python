'''
8.3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение
 должен контролировать типы данных элементов списка.
'''

class Errors(ValueError):
    def __init__(self, txt):
        self.txt = txt

my_lst = []

while True:
    userAnswer = input("Введите числовое значение для списка: ")
    if userAnswer == "*":
        break
    try:
        if userAnswer.isdigit() is False:
            raise Errors("Вы ввели текст")
        else:
            userAnswer = int(userAnswer)
            my_lst.append(userAnswer)
    except Errors as err:
        print(err)
    except Exception:
        print("Error")



print(f"Конец программы.\n {my_lst}")