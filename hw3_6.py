# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}.

# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    __wage_dict = {'wage': 0, 'bonus': 0}
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = self.__wage_dict
        self.__income['wage'] = wage
        self.__income['bonus'] = bonus

    def getWage(self):
        return self.__income['wage']

    def getBonus(self):
        return self.__income['bonus']

class Position(Worker):
    def get_full_name(self):
        fullname = f'{self.name} {self.surname}'
        print(f'Полное имя: {fullname}')

    def get_total_income(self):
        full_wage = f"{self.getWage() + self.getBonus()}"
        print(f'Доход с учетом премии: {full_wage}')


a = Position('Вася','Иванов','dev', 200, 20)
a.get_full_name()
a.get_total_income()
