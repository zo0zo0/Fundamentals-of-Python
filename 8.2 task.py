'''
8.2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
'''

class Errors(ZeroDivisionError):
    def __init__(self, user_data):
        self.user_data = user_data

user_answer = input("Введите делимое и делитель для примера: ")
user_answer = user_answer.split(" ")

try:
    if int(user_answer[1]) == 0:
        raise Errors("Вы ввели делитель в качестве нуля")
    else:
        sample_calcul = int(user_answer[0]) / int(user_answer[1])
except Errors as err:
    print(err)
except ValueError:
    print("Вы ввели текст")
else:
    print(user_answer, sample_calcul)

#ValueError: - текст
#ZeroDivisionError: - ноль
