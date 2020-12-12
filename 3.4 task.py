'''
3.4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''

print("1ый вариант решения ------>")

def my_func(x, y):
    system_calculation = int(x) ** int(y)
    return system_calculation

user_lst = []
for i in range(2):
    user_answer = input(f"Введите {i + 1} число для программы: ")
    user_lst.append(user_answer)

system_answer = my_func(user_lst[0], user_lst[1])
print(f"Х[{user_lst[0]}] в степени Y[{user_lst[1]}] = {system_answer}")


print("\n2ой вариант решения ------>")

def my_func2(x, y):
    nex_x = 1
    for b in range(int(y)):
        new_x = nex_x * int(x)
    return new_x

user_lst2 = []
for i in range(2):
    user_answer2 = input(f"Введите {i + 1} число для программы: ")
    user_lst2.append(user_answer2)

system_answer2 = my_func(user_lst2[0], user_lst2[1])
print(f"Х[{user_lst2[0]}] в степени Y[{user_lst2[1]}] = {system_answer2}")

# END of program - zo0