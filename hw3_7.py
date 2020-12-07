# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству ячеек (целое число). В классе должны быть реализованы
# методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(6), принимающий экземпляр класса и количество ячеек в ряду. Данный
# метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
# вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет
# строку: *****\n*****\n*****.

class Cell:
    def __init__(self, count):
        self.box = count

    def __add__(self, other):
       return Cell(self.box + other.box)

    def __sub__(self, other):
        if self.box - other.box < 0:
            print('Неудача')
        else:
            return Cell(self.box - other.box)

    def __mul__(self, other):
        return Cell(self.box * other.box)

    def __truediv__(self, other):
        return Cell(self.box // other.box)

    def __str__(self):
        return f'{self.box}'

    def make_order(self, cell_count):
        self.cell_count = cell_count
        while self.box > 0:
            if self.box > cell_count:
                print('*' * cell_count)
            else:
                print('*' * self.box)
            self.box = self.box - cell_count


a = Cell(12)
b = Cell(4)
c = Cell(6)

print(a + b)
(a+b).make_order(5)

