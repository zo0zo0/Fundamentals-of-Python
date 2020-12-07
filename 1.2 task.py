#Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_answer_time = int(input("Введите количество секунд:"))

system_hours = user_answer_time // 3600
system_minutes = (user_answer_time % 3600) // 60
system_seconds = (user_answer_time % 3600) % 60

print(f"Время в формате чч:мм:сс составляет: {system_hours}:{system_minutes}:{system_seconds}")
