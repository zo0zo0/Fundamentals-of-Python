'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
with open(file="5.6_task.txt", encoding="UTF-8", mode="r") as file_56:
    lst_for_adding = []
    second_lst = []
    amount_for_el = 0
    task_dict = {}
    for line in file_56:
        lst_for_adding.append(line.split())
    for el in lst_for_adding:
        for i in range(len(el)):
            if i == 0:
                continue
            elif el[i] == "—":
                continue
            amount_for_el = amount_for_el + int(el[i])
        second_lst.append(amount_for_el)
        amount_for_el = 0
    for b in range(len(second_lst)):
        task_dict[lst_for_adding[b][0]] = second_lst[b]

    print(f"Общее число количество занятий на уровне предмета: {task_dict}")


