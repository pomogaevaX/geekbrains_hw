# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
# «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
# на уроках по ООП.

default_place = 'приход'


class OfficeEquipment:
    def __init__(self, type, number, place):
        self.type = type
        self.number = number
        self.place = place


class OfficeStore:
    def __init__(self):
        self.store_dict = {}

    def take(self, tech: OfficeEquipment):
        key = f'{tech.number} {tech.type}'
        if self.store_dict.get(key, 'no') == 'yes':
            print('Товар уже есть на складе')
        else:
            self.store_dict[key] = 'yes'
            tech.place = 'склад'
            print(f'Товар {key} отправлен на склад')

    def send_to_dep(self, tech: OfficeEquipment, department):
        key = f'{tech.number} {tech.type}'
        if self.store_dict.get(key, 'no') == 'no':
            print('Товара нет на складе')
        else:
            del self.store_dict[key]
            tech.place = department
            print(f'Товар {key} отправлен в {department}')


class Print(OfficeEquipment):
    def __init__(self, numb, cartridge_type):
        super().__init__('print', numb, default_place)
        self.cartridge_type = cartridge_type


class Scanner(OfficeEquipment):
    def __init__(self, numb, scan_speed):
        super().__init__('scanner', numb, default_place)
        self.scan_speed = scan_speed


class Xerox(OfficeEquipment):
    def __init__(self, numb, model):
        super().__init__('xerox', numb, default_place)
        self.model = model

b = Print(111,'hjgjhj')
c = Scanner(111,'ybuyh')
n = Scanner(111,'ybuyh')
v = Xerox(654,'ybuyh')
a = OfficeStore()
a.take(b)
a.take(c)
a.take(v)
a.take(n)
a.send_to_dep(c,'aaaaaa')
a.send_to_dep(v,'bbbbbb')
a.send_to_dep(b,'bbbbbb')