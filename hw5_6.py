# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self, text):
        print(f"Запуск отрисовки {text}")


class Pen(Stationery):
    def __init__(self):
        Stationery.__init__(self, 'pen')

    def draw(self):
        Stationery.draw(self, 'ручкой')

class Pencil(Stationery):
    def __init__(self):
        Stationery.__init__(self, 'pencil')

    def draw(self):
        Stationery.draw(self, 'карандашом')

class Handle(Stationery):
    def __init__(self):
        Stationery.__init__(self, 'handle')

    def draw(self):
        Stationery.draw(self, 'маркером')

a = Handle()
a.draw()

b = Pencil()
b.draw()

c = Pen()
c.draw()



