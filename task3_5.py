# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

money = []
n = 0
with open('employees', 'r') as file_emp:
    lines = file_emp.readlines()

    for line in lines:
        n += 1
        name, sal = line.split(":")
        sal = int(sal)
        money.append(sal)
        if sal < 20000:
            print(name)

    print(f'Средний доход: {sum(money) / n}')




