'''
5.3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.
'''

with open(file="5.3_task.txt", encoding="UTF-8", mode="r") as file_5_3:
    lst_name = []
    salary_list = []
    average_salary = 0
    for line in file_5_3:
        lst_name.append(line.split())
    for i in range(len(lst_name)):
        lst_name[i][1] = int(lst_name[i][1])
        average_salary = average_salary + int(lst_name[i][1])
        if lst_name[i][1] < 20000:
            salary_list.append(lst_name[i])
    salary_list = dict(salary_list)
    amount_for_calc = int(len(salary_list))
    print(f'Список фамилий с зп меньше 20000: {salary_list.keys()}\n'
          f'Средняя величина дохода всех сотрудников = {average_salary / len(lst_name)}')