# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:

    def __init__(self, date):
        self.date = date

    @classmethod
    def date_outside(cls, dateArg:str):
        date = int(''.join(c for c in dateArg if c.isdigit()))
        print(f'Тип {type(date)}')
        return date

    @staticmethod
    def date_validate(date_val:str):
        list_val = []
        list_val = date_val.split('-')
        date = int(list_val[0])
        month = int(list_val[1])
        year = int(list_val[2])
        if date <= 31 and date > 0 and month <= 12 and month > 0 and year <= 99 and year > 0:
            print(f'Дата {date_val} корректна')
        else:
            print('Неверный формат даты')




print( f'{Data.date_outside("23-12-20")}')
print( f'{Data.date_validate("23-12-20")}')