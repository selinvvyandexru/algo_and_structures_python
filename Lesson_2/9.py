"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def user_input():
    """Пользовательский ввод"""
    try:
        num = int(input('-->'))
    except ValueError:
        return 'err'
    else:
        return num


def user_dialog(num='err'):
    """Пользовательский диалог"""
    while num == 'err':
        print('Введите любое натуральное '
              'число или 0 для завершения:')
        num = user_input()
        if num == 'err':
            print('Нужно вводить только '
                  'цифры. Повторите ввод.')
    return num


def num_count_recurs(sav=0, snm=0):
    """Суммирование цифр числа через
    рекурсию"""
    num = user_dialog()
    if num == 0:
        return sav, snm
    tmp = 0
    tnm = num
    while tnm != 0:
        cou = tnm % 10
        tmp += cou
        tnm //= 10
    if tmp > sav:
        sav = tmp
        snm = num
    return num_count_recurs(sav, snm)


def num_count_cycle(num=-1, sav=-1):
    """Суммирование цифр числа
    через цикл"""
    while num != 0:
        num = user_dialog()
        tmp = 0
        tnm = num
        while tnm != 0:
            cou = tnm % 10
            tmp += cou
            tnm //= 10
        if tmp > sav:
            sav = tmp
            snm = num
    return sav, snm


SAV, SNM = num_count_recurs()
if SNM != 0:
    print(f'Число с максимальной суммой цифр {SNM}. '
          f'\nСумма цифр составляет {SAV}.')
else:
    print('OK')
