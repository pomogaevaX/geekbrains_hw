# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.
import random

class Matrix():
    def __init__(self, size):
        self.size = size
        list_matrix = []
        for i in range(size):
            list_matrix.append([])
            for j in range(size):
                list_matrix[i].append(random.randint(0, 9))
        self.list_matrix = list_matrix

    def __str__(self):
        matrix_str = ' '
        for i in range(self.size):
            for j in range(self.size):
                matrix_str = matrix_str + f'{self.list_matrix[i][j]} '
            matrix_str += "\n"
        return matrix_str

    def __add__(self, other):
        res = Matrix(self.size)
        if self.size != other.size:
            return "Ошибка операции"
        for i in range(self.size):
            for j in range(self.size):
                res.list_matrix[i][j] = self.list_matrix[i][j] + other.list_matrix[i][j]
        return res


s = Matrix(2)
d = Matrix(2)

print(s)
print(d)
print(s+d)