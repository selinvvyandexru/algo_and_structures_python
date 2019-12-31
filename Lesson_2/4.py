"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def sum_range(vol, num, smm):
    """Суммирует числа ряда"""
    if num == 0:
        return smm
    vol /= -2
    smm += vol
    num -= 1
    return sum_range(vol, num, smm)


try:
    NUM = int(input('Введите количество элементов для подсчета: '))
except ValueError:
    print('Надо было ввести целое число.')
else:
    print(sum_range(-2, NUM, 0))
