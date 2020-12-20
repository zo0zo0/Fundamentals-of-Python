'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''

list_rus = ["Один", "Два", "Три", "Четыре"]
with open(file="5.4_task.txt", encoding="UTF-8", mode="r") as file_5_4:
    list_54 = []
    for line in file_5_4:
        list_54.append(line.split())
    for i in range(len(list_54)):
        list_54[i][0] = list_rus[i]
    print(list_54)
with open(file="5.4_task_rus.txt", encoding="UTF-8", mode="w") as file_5_4_rus:
    file_5_4_rus.write(str(list_54))