'''
6.5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
'''


class stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки. {self.title}')


class pen(stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск ручной рисовки. {self.title}')


class pencil(stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск карандашовки. {self.title}')


class handle(stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск маркировки "Честный знак". {self.title}')

p = pencil("Рисуем карандашом")
pen = pen("Рисуем ручкой")
h = handle("Рисуем маркером")