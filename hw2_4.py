# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# for i in first_list:
new_list = [first_list[i] for i in range(1, len(first_list)) if first_list[i] > first_list[i-1]]
print(first_list)
print(new_list)