# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.


import json
dict = {}
firms_list = []
a = 0
middle_profit = 0
with open('firms', 'r', encoding='UTF-8') as firms_file:
    for line in firms_file:
        #чтение инфо о фирмах, подсчет значений:
        name, type, proceeds, cost = line.split(' ')
        proceeds = int(proceeds)
        cost = int(cost)
        profit = proceeds - cost
        dict [name] = abs(profit)
        if profit >= 0:
            middle_profit += profit
            a += 1
    #заполнение списка данными о каждой фирме, расчет средней прибыли, добавление в список:
    firms_list.append(dict)
    dict_average_profit = {}
    dict_average_profit['average_profit'] = middle_profit / a
    firms_list.append(dict_average_profit)
    print(firms_list)
    # создание и запись json:
    json_list = json.dumps(firms_list)
with open('file.json', 'w') as json_file:
    json_file.write(json_list)
