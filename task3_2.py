# Задание 3
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# решение через dict

from time import sleep

year = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль',
        8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
user_count = int(input('Введите номер месяца: '))
if year.get(user_count) == "январь" or year.get(user_count) == "февраль" or year.get(user_count) == "декабрь":
    print('Это зимний месяц')
elif year.get(user_count) == "март" or year.get(user_count) == "апрель" or year.get(user_count) == "май":
    print('Это весенний месяц')
elif year.get(user_count) == "июнь" or year.get(user_count) == "июль" or year.get(user_count) == "август":
    print('Это летний месяц')
elif year.get(user_count) == "сентябрь" or year.get(user_count) == "октябрь" or year.get(user_count) == "ноябрь":
    print('Это осенний месяц')
sleep(1)

# решение через list
user_count = int(input('Введите номер месяца: '))
list_year = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
if list_year[user_count] == "январь" or list_year[user_count] == "февраль" or list_year[user_count] == "декабрь":
    print('Это зимний месяц')
elif list_year[user_count] == "март" or list_year[user_count] == "апрель" or list_year[user_count] == "май":
    print('Это весенний месяц')
elif list_year[user_count] == "июнь" or list_year[user_count] == "июль" or list_year[user_count] == "август":
    print('Это летний месяц')
elif list_year[user_count] == "сентябрь" or list_year[user_count] == "октябрь" or list_year[user_count] == "ноябрь":
    print('Это осенний месяц')
