'''
2.2 Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
элементов необходимо использовать функцию input().
'''

elements_qty = int(input("Введите количество используемых элементов в списке: "))
list_with_elements = []
for i in range(elements_qty):
    element_for_list = input(f"Введите {i+1}й элемент для списка\n")
    list_with_elements.append(element_for_list)
print(f"Ваш список из элементов состоит из {list_with_elements}\n")

for i in range(1, len(list_with_elements), 2):
    list_with_elements[i], list_with_elements[i-1] = list_with_elements[i-1], list_with_elements[i]
print(f"Ваш список из элементов преобразовался в {list_with_elements}")

# END of program - zo0