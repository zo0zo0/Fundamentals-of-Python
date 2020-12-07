#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_answer_figure = input("Введите число n для расчета по формуле: ")

system_answer1 = user_answer_figure + user_answer_figure
system_answer2 = user_answer_figure + user_answer_figure + user_answer_figure

user_answer_figure = int(user_answer_figure)
system_answer1 = int(system_answer1)
system_answer2 = int(system_answer2)

print(f"Ваша сумма n + nn + nnn чисел ровняется : {user_answer_figure + system_answer1 + system_answer2}")