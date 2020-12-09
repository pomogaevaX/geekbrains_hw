# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
# перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumb:
    def __init__(self, complex_numb_a, complex_numb_b):
        self.complex_numb_a = complex_numb_a
        self.complex_numb_b = complex_numb_b

    def __add__(self, other):
        sum_complex = ComplexNumb((self.complex_numb_a + other.complex_numb_a), (self.complex_numb_b + other.complex_numb_b))
        return sum_complex

    def __str__(self):
        return f'{self.complex_numb_a} + {self.complex_numb_b}j'

    def __mul__(self, other):
        a = self.complex_numb_a
        b = self.complex_numb_b
        c = other.complex_numb_a
        d = other.complex_numb_b
        mul_complex = ComplexNumb((a * c - b * d), (a * d + b * c))
        return mul_complex


n = ComplexNumb(1, 2)
p = ComplexNumb(1, 2)
q = ComplexNumb(1, 1)
print(n+p+q)
print(n*p)
