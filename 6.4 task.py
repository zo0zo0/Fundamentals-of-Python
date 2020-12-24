'''
6.4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево)
. А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
. Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
'''

class car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed  #максимальная скорость
        self.current_speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, time_for_process):
        self.current_speed = time_for_process * 10
        if self.current_speed >= self.speed:
            self.current_speed = self.speed
        print(f"Машина поехала. И за {time_for_process} сек. разогналась до {self.current_speed} км/ч")

    def stop(self, time_for_process):
        self.current_speed = self.current_speed - (10 * time_for_process)
        if self.current_speed <= 0:
            print(f"Машина остановилась")
        else:
            print("Понадобилось еще несколько секунд для остановки машины и в конечном итоге машина остановилась")
        self.current_speed = 0

    def turn(self, move_to_side):
        if self.current_speed == 0:
            print(f"Ваша скорость = 0 . Запустите сначала машину")
        else:
            print(f"Машина на скорости {self.current_speed} км/ч повернула {move_to_side}")

    def show_speed(self):
        print(f"Ваша текущая скорость = {self.current_speed} км/ч")

class TownCar(car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.current_speed > 60:
            print(f"Вы превышаете скорость! Вам необходимо снизить скорость до 60 км/ч. Ваша текущая "
                  f"скорость = {self.current_speed} км/ч")
        else:
            print(f"Ваша текущая скорость = {self.current_speed} км/ч")

class SportCar(car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.current_speed > 40:
            print(f"Вы превышаете скорость! Вам необходимо снизить скорость до 40 км/ч. Ваша текущая "
                  f"скорость = {self.current_speed} км/ч")
        else:
            print(f"Ваша текущая скорость = {self.current_speed} км/ч")

class PoliceCar(car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(150, "Желтый Металлик", "Ford Focus", False)
sport_car = SportCar(250, "Белый", "Porshe", False)
work_car = WorkCar(120, "Синий", "ЗИЛ", False)
police_car = PoliceCar(180, "Синий и Белый", "Mazda", True)