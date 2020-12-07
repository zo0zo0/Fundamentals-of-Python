# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел
# и строк и сохраните в переменные, выведите на экран.

#user_answer_figure1 = int(input("Введи 1ое число:"))
#user_answer_str1 = input("Введи 1ый текст:")
#user_answer_figure2 = int(input("Введи 2ое число:"))
#user_answer_str2 = input("Введи ой текст:")


#print("Ваши числа: ", user_answer_figure1, ", ", user_answer_figure2)
#print("Ваш текст: ", user_answer_str1, ", ", user_answer_str2)

i = 1
while i <= 3:
    user_answer_figure = int(input("Введи число:"))
    user_answer_str = input("Введи текст:")
    print("Ваше число: ", user_answer_figure, "и  Ваш текст: ", user_answer_str)
    i = i + 1
print("Конец проги")
