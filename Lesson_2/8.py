"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def user_input():
    """Пользовательский ввод"""
    try:
        num = int(input('-->'))
    except ValueError:
        return 'err'
    else:
        return num


def user_dialog(stg='err', num='err'):
    """Пользовательский диалог"""
    while stg == 'err':
        print('Введите любую последовательность цифр:')
        stg = user_input()
        if stg == 'err':
            print('Нужно вводить только цифры. Повторите ввод.')
    while num == 'err':
        print('Введите искомую цифру:')
        num = user_input()
        if num == 'err':
            print('Нужно ввести цифру. Повторите ввод.')
    return stg, num


def num_count_recurs(stg, num, cou):
    """Подсчет искомой цифры
    через рекурсию"""
    if stg == 0:
        return cou
    res = stg % 10
    if res == num:
        cou += 1
    stg //= 10
    return num_count_recurs(stg, num, cou)


def num_count_cycle(stg, num, cou=0):
    """Подсчет искомой цифры
    в цикле"""
    while stg != 0:
        res = stg % 10
        if res == num:
            cou += 1
        stg //= 10
    return cou


STG, NUM = user_dialog()
print(f'Во введенной последовательности, '
      f'цифра {NUM} встречается:')
print(f'- счет через рекурсию: {num_count_recurs(STG, NUM, 0)}')
print(f'- подсчет через цикл:  {num_count_cycle(STG, NUM)}')
