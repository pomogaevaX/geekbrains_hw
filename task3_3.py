# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    my_list = list()
    my_list.append(x)
    my_list.append(y)
    my_list.append(z)
    print(my_list)
    my_list = sorted(my_list)
    print(my_list)
    return my_list[1] + my_list[2]

a = int(input("Введите 1 значение: "))
b = int(input("Введите 2 значение: "))
c = int(input("Введите 3 значение: "))
print(f'Сумма: {my_func(a, b, c)}')
