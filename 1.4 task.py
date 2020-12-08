#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_answer = -1
user_answer = int(user_answer)
while user_answer < 0 :
    user_answer = int(input("Введите целое положительное число: "))

qty_of_len = int(len(str(user_answer)))

score = 0
i = 0
while i <= qty_of_len - 1:
    user_division = int(user_answer % 10)
    user_answer = int(user_answer / 10)
    i = i + 1
    if score <= user_division:
        score = user_division


print(f"Максимальное число является: {score}")
