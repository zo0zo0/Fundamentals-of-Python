'''
3.3 Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
наибольших двух аргументов.
'''

def my_func(number1, number2, number3):
    new_lst = [number1, number2, number3]
    new_lst.sort()
    lst_max_amount = int(new_lst[-1]) + int(new_lst[-2])
    return lst_max_amount

user_lst = []
for i in range(3):
    user_answer = input(f"Введите {i+1}е число для программы: ")
    user_lst.append(user_answer)

system_amount = my_func(user_lst[0], user_lst[1], user_lst[2])

print(f"Сумма наибольших двух аргументов составляет: {system_amount}")

# END of program - zo0