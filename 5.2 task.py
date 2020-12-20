'''
5.2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

with open(file="5.2_task.txt", encoding="UTF-8", mode="r") as file_text:
    str_i = 0
    for line in file_text:
        str_i += 1
        print(f"Количество слов в строке {str_i} составляет: {len(line.split())}")
    print(f"Количество строк = {str_i}")