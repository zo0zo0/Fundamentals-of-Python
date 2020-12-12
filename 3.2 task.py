'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

def function_User1(name, surname, birthdate, city, email, telephone):
    print(f'Информация о пользователе: "Имя" - {name}, "Фамилия" - {surname}, "Год рождения" - {birthdate}, "Город проживания" - {city}, "email" - {email}, "Телефон" - {telephone}')

questions_user1 = "Имени", "Фамилии", "Года рождения", "Города проживания", "email", "Телефон"

lst_for_function1 = []
for i in range(len(questions_user1)):
    lst_for_function1.append(input(f"Введите данные о {questions_user1[i]} пользователя: "))

lst_for_function1 = tuple(lst_for_function1)

function_User1(name=lst_for_function1[0], surname=lst_for_function1[1], birthdate=lst_for_function1[2], city=lst_for_function1[3], email=lst_for_function1[4], telephone=lst_for_function1[5])




#2ой вариант решения
print("2nd variant   ---->")
def function_User(*args, **kwargs):
    print(f"Информация о пользователе: {args} \n {kwargs}")

questions_user = "Имени", "Фамилии", "Года рождения", "Города проживания", "email", "Телефон"

lst_for_function = []
for i in range(len(questions_user)):
    lst_for_function.append(input(f"Введите данные о {questions_user[i]} пользователя: "))

function_User(tuple(lst_for_function))

# END of program - zo0