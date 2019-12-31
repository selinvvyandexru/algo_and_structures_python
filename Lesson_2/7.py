"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""
import sys
sys.setrecursionlimit(3150)


def n_sum_recurs(num, smm):
    """Суммирует числа от 1 до num
        через рекурсию"""
    if num == 0:
        return smm
    smm += num
    num -= 1
    return n_sum_recurs(num, smm)


def n_sum_cycle(num):
    """Суммирует числа от 1 до num
        через цикл"""
    smm = 0
    for i in range(num):
        smm += i + 1
    return smm


try:
    NUM = int(input('Введите целое число от 1 до 3000: '))
except ValueError:
    print('Ошибка. Введено неверное значение.')
else:
    if 1 <= NUM <= 3000:
        if (n_sum_recurs(NUM, 0) == NUM * (NUM + 1) / 2
                and n_sum_cycle(NUM) == NUM * (NUM + 1) / 2):
            print('Выражение 1+2+...+n = n(n+1)/2 верно.')
        else:
            print('Выражение 1+2+...+n = n(n+1)/2 неверно.')
    else:
        print('Ошибка. Введено неверное значение.')
