# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

lt = []
a = '1 2 3 4 5'
with open('file_for_task5.txt', 'w', encoding='UTF-8') as text:
    text.write(a)
with open('file_for_task5.txt', 'r', encoding='UTF-8') as text:
    n = text.read()
    print(f'Числа записанные в файл: {n}')
    lt = n.split(' ')
    p = 0
    for i in lt:
       p += int(i)
    print(f"Сумма чисел, записанных в файл: {p}")

