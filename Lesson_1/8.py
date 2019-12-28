""" 8.	Определить, является ли год, который ввел пользователем,
 високосным или не високосным.
Год является високосным в двух случаях: либо он кратен 4,
 но при этом не кратен 100, либо кратен 400."""

YEAR = input('Введите год в формате YYYY: ').strip()
if (len(YEAR) == 4
        and YEAR.isdigit()
        and YEAR != '0000'):
    YEAR = int(YEAR)
else:
    YEAR = None

if YEAR is None:
    print('Ошибка в данных.')
elif YEAR % 400 == 0:
    print('Год високосный.')
elif YEAR % 4 == 0 and YEAR % 100 != 0:
    print('Год високосный.')
else:
    print('Год не високосный.')
