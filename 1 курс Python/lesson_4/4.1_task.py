'''
4.1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
'''

from sys import argv

def fun_cacl_salary(hours, salary_hour, benefit):
    amount2 = (hours * salary_hour) + benefit
    return amount2

print("Имя скрипта: ", argv[0])
print("Выработка в часах: ", argv[1])
print("Ставка в час: ", argv[2])
print("Премия: ", argv[3])

amount = fun_cacl_salary(int(argv[1]), int(argv[2]), int(argv[3]))

print(f"Расчет заработной платы сотрудника: {amount}")