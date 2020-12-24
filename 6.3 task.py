'''
6.3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
'''

class worker():

    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"salary": salary, "bonus": bonus}

class position(worker):
    def __init__(self, name, surname, position, salary, bonus):
        self.type = "level1"
        super().__init__(name, surname, position, salary, bonus)

    def get_full_name(self):
        a_and_b = self.name + " " + self.surname
        return a_and_b

    def get_total_income(self):
        amount = self._income["salary"] + self._income["bonus"]
        return amount

employee = position("Boris", "Samailov", "Manager", 140000, 70000)