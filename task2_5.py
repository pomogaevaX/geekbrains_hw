# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

lines = 0
words = 0
with open('my_file2', 'w') as new_file:
    new_file.write('мама мыла раму\n')
    new_file.write('привет, мир\n')
    new_file.write('конфета\n')
with open('my_file2', 'r') as new_file:
    for line in new_file:
        lines += 1
        words = line.count(' ') + 1
        print(f'Строка:{lines} Слов в строке:{words}')
print(f'Всего строк: {lines}')

