#Задача 4: Пользователь вводит целое положительное число.
#Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

max_count = 0
a = int(input('Введите целое положительное число: '))
if a >= 0 and isinstance(a, int):
    while a >= 10:
        b = a % 10
        a = a // 10
        if b > max_count:
            max_count = b
else:
    print('Неверное значение! Введите целое положительное число, например, 12')
    a = int(input("Повторите ввод: "))
    while a >= 10:
        b = a % 10
        a = a // 10
        if b > max_count:
            max_count = b

if max_count > a:
    print(f'Самая большая цифра: {max_count}')
else: print(f'Самая большая цифра: {a}')
