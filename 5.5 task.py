'''
5.5 Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
'''

import random

with open(file="5.5_task.txt", encoding="UTF-8", mode="w") as file_5_5:
    i = 1
    while i <= 5 :
        file_5_5.write(str(round(random.random() * 100, 2)) + " ")
        i += 1

with open(file="5.5_task.txt", encoding="UTF-8", mode="r") as file_5_5:
    amount = []
    rez = 0
    for line in file_5_5:
        amount.append(line.split())
    print(amount)
    for i in range(len(amount[0])):
        rez = rez + float(amount[0][i])
    print(f"Сумма чисел c округлением = {round(rez, 2)}")
    print(file_5_5.read())