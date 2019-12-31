"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


def eve_odd(eve, odd, num):
    """Определяет четность цифры и
    ведет подсчет"""
    if num == 0:
        return eve, odd
    if num & 1:
        odd += 1
    else:
        eve += 1
    num = num // 10
    return eve_odd(eve, odd, num)


EVE, ODD = 0, 0
try:
    NUM = int(input('Введите целое число: '))
except ValueError:
    print('Ошибка. Внимательнее вводите число.')
else:
    EVE, ODD = eve_odd(EVE, ODD, NUM)
    print(f'Четных - {EVE}, нечетных - {ODD}')
