'''
2.3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
'''
#                  1        2       3       4           5       6       7       8       9        10      11      12
month_seasons = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
dict_seasons = {1:"Зима", 2:"Зима", 3:"Весна", 4:"Весна", 5:"Весна", 6:"Лето", 7:"Лето", 8:"Лето", 9:"Осень", 10:"Осень", 11:"Осень", 12:"Зима"}

user_answer = int(input("Введите в виде целого числа от 1 до 12 месяц: "))
print(f"Реализация списком: Указанный числовой месяц относится ко времени года: {month_seasons [user_answer - 1]}")
print(f"Реализация через словарь: Указанный числовой месяц относится ко времени года: {dict_seasons [user_answer]}")

# END of program - zo0