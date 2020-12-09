# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.


list = []
with open('file_for_task4', 'r', encoding='UTF-8') as count:
    for line in count:
        line = line.replace('One','Один')
        line = line.replace('Two', 'Два')
        line = line.replace('Three', 'Три')
        line = line.replace('Four', 'Четыре')
        print(line)
        list.append(line)

with open('file_for_task4_new.txt', 'r+', encoding='UTF-8') as wr_file:
    for el in list:
        wr_file.write(f'{el}\n')
