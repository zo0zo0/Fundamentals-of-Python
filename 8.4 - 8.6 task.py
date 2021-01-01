'''
8.4-8.6. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

'''

class Office_equipment():
    def __init__(self, eqName, eqPrice, eqSizes, processColour, quantity, *args):
        self.eqName = eqName #наименование товарной позиции
        self.eqPrice = eqPrice #цена товарной позиции
        self.eqSizes = eqSizes #размер техники
        self.processColour = processColour  #цветопередача: ЧБ, цветная
        self.quantity = quantity
        self.storage_full = []
        self.storage_ini = []
        self.dict_unit = {'Модель устройства': self.eqName, 'Цена устройства': self.eqPrice,
                          "Размер усройства": self.eqSizes, "Цветопередача": self.processColour,
                          "Количество": self.quantity}

    def __str__(self):
        return f'Модель устройства: {self.eqName}, Цена устройства: {self.eqPrice}, ' \
               f'Размер усройства: {self.eqSizes}, Цветопередача: {self.processColour},' \
               f'Количество: {self.quantity}'

class Warehouse():

    def __init__(self):
        self.storage = 30 #кол-во дней на хранение товара по бизнес процессу
        self.capacity = 12000 #вместимость техники, кол-во штук
        self.delivery = 3 #кол-во дней, доставка до магазина/клиента
        super().__init__(eqName, eqPrice, eqSizes, processColour, quantity)

    @property
    def warehouse_acceptance(self):
        try:
            eqName = input('Введите наименование')
            eqPrice = int(input('Введите цену'))
            eqSizes = input('Введите размеры')
            processColour = input('Введите цветопередачу')
            quantity = int(input('Введите количество'))
            groupage = {'Модель устройства': eqName, 'Цена устройства': eqPrice,
                          "Размер усройства": eqSizes, "Цветопередача": processColour,
                          "Количество": quantity}
            if self.capacity - quantity < 0:
                print("Товар не может быть доставлен на склад, т.к. склад переполнен")
            else:
                self.capacity = self.capacity - quantity
                self.dict_unit.update(groupage)
                self.storage_ini.append(self.dict_unit)
                print(f'Актуальный список для добавления: \n {self.storage_ini}')
        except:
            return f'Ошибка при вводе данных или склад переполнен'

        try:
            self.storage_full.append(self.storage_ini)
            print(f"На складе сейчас: \n {self.storage_full} \n"
                f"Остаток вмещаемости склада составляет {self.capacity}")
        except:
            return f'Ошибка при вводе данных или склад переполнен'

    def shipment_toBranch(self):
        try:
            print(self.storage_full[0])
        except:
            print("На складе нет товаров для отправки в филиалы")
        branch_toSend = input('Введите наименование филиала для отправки')
        print(f"Выберите товары со склада для отправки: \n {self.storage_full}")
        eqName = input("Введите имя позиции")
        quantity = int(input('Введите количество'))
        try:
            for el in self.storage_full:
                if el['Модель устройства'] == eqName and el["Количество"] >= quantity:
                    print(f"Количество есть на складе и в следующей поставке отправим на филиал {branch_toSend}")
                else:
                    print("Такой позиции нет или не хватает количества для отправки")
        except:
            print(f'Товар на складе: \n {self.storage_full}')


class Printer(Office_equipment, Warehouse):
    def __init__(self, eqName, eqPrice, eqSizes, processColour, quantity):
        self.printer_Functional = "Используется исключительно для печати документов"
        super().__init__(eqName, eqPrice, eqSizes, processColour, quantity)


class Scaner(Office_equipment, Warehouse):
    def __init__(self, eqName, eqPrice, eqSizes, processColour, quantity):
        self.scaner_Functional = "Используется исключительно для сканирования документов"
        super().__init__(eqName, eqPrice, eqSizes, processColour, quantity)


class Xerox(Office_equipment, Warehouse):
    def __init__(self, eqName, eqPrice, eqSizes, processColour, quantity):
        self.xerox_Functional = "Используется для сканирования, печати и скан-печати документов"
        super().__init__(eqName, eqPrice, eqSizes, processColour, quantity)


pr = Printer("HP LaserJet 1070", 3490, "50x38x65", "Цветная", 30)
sc = Scaner("Ericson SuperScan 3", 2600, "45x50x65", "Цветная", 15)
xer = Xerox("Canon", 15000, "87x76x150", "Цветная", 45)