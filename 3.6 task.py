'''
3.6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''

def int_func(text):
    world_lst = []
    for i in range(len(text)):
        system_text = text[i].capitalize()
        world_lst.append(system_text)
    return world_lst

user_text = input("Введите слово с маленькой буквой: ")
user_str = user_text.split()
print(int_func(user_str))

user_text = input("Введите строку из слов: ")
user_str = user_text.split()
print(int_func(user_str))

# END of program - zo0