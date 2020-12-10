'''
2.4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
'''

user_str = input("Введите строку из нескольких слов, разделённых пробелами: ").split()
user_len = len(user_str)
#lst = list(user_str)

print("\nВывести каждое слово с новой строки:")
for i in range(user_len):
    print(f"{user_str[i]}")

print("\nСтроки необходимо пронумеровать:")
for i in range(user_len):
    print(f"{i + 1} - {user_str[i]}")

print("\nЕсли слово длинное, выводить только первые 10 букв в слове:")
for i in range(user_len):
    if len(user_str[i]) >= 10:
        print(f"{i + 1} - {str(user_str[i])[0:10]}")
        continue
    print(f"{i + 1} - {user_str[i]}")

# END of program - zo0

