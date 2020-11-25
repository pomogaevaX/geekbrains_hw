# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f_1 = open("my_file.txt", 'w', encoding='UTF-8')
while True:
    user_text = input("Введите строку для записи в файл: ")
    if not user_text:
        break
    f_1.write(user_text + '\n')
f_1.close()
f_1 = open("my_file.txt", 'r')
print(f_1.read())
f_1.close()
