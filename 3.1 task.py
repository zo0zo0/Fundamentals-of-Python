'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
 пользователя, предусмотреть обработку ситуации деления на ноль.

'''

def fun_division(amount_1, amount_2):
    try:
        divided = amount_1 / amount_2
        print(f"Значение деления = {divided}")
    except ZeroDivisionError:
        print("Деление на ноль")
    finally:
        print("Переход на новую итерацию")


while True:
    a = input("Введите первое число: ")
    b = input("Введите первое число: ")

    if a == "":
        print("Вы покинули цикл")
        break

    a = int(a)
    b = int(b)
    fun_division(a, b)


# END of program - zo0