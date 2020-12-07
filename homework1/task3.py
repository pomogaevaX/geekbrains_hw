# Задача 3: Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_param = int(input('Введите целое число: '))
print(f'Вы ввели: {user_param}. Сумма для этого числа: {user_param} + '
      f'{2 * user_param} + {3 * user_param} = {user_param}{user_param * 2}{user_param * 3}')