'''
4.2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''


lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

lst_new = [lst[i] for i in range(lst[1], len(lst)) if lst[i] > lst[i-1]]

print(lst_new)

