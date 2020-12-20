'''
5.7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. (прибыль — выручка
больше издержек, или убыток — издержки больше выручки).Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''
import json

with open(file="5.7_task.txt", encoding="UTF-8", mode="r") as file_57:
    lst_common = []
    lst_firms = {}
    average_profit = 0
    av_dict_profit = {}
    lst_general = []
    prof_count = 0
    for line in file_57:
        lst_common.append(line.split())
    for el in lst_common:
        f_amount = 0
        f_amount = int(el[2]) - int(el[3])
        if f_amount > 0:
            lst_firms[el[0]] = f_amount
            average_profit = average_profit + f_amount
            prof_count += 1
        else:
            lst_firms[el[0]] = f_amount
    av_dict_profit['Average profit'] = round(average_profit / prof_count)

    lst_general.append(lst_firms)
    lst_general.append(av_dict_profit)

    with open(file="5.7_task.json", encoding="UTF-8", mode="w") as file_json57:
        json.dump(lst_general, file_json57)
