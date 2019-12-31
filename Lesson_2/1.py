# coding=utf-8
"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""


def user_input(dtp):
    """Принимает введенные значения,
    производит проверку и преобразование к нужному типу"""
    if dtp == '0':
        return None
    vol = input('-->')
    try:
        if dtp == 'f':
            if ',' in vol:
                vol = vol.replace(',', '.')
                print('ПРЕДУПРЕЖДЕНИЕ.'
                      '\nДробная часть должна быть отделена точкой!'
                      '\nПроверьте раскладку клавиатуры.')
            vol = float(vol)
        elif dtp == 's':
            if vol == '0':
                return None
            if vol not in ('+', '-', '/', '*'):
                vol = 'err'
        return vol
    except (ValueError, TypeError):
        vol = 'err'
        return vol


def user_dialog(fst='err', sign='err', sec='err'):
    """Сообщения пользователю"""
    print('Введите первое число:')
    while fst == 'err':
        fst = user_input('f')
        if fst == 'err':
            print('Значение введено неверно, повторите:')
    print('Введите знак действия:')
    while sign == 'err':
        sign = user_input('s')
        if sign == 'err':
            print('Вы ввели неверный знак '
                  '(надо + - * / или 0 для завершения)')
            print('Повторите ввод знака:')
        if sign is None:
            return 1, sign, 1
    print('Введите второе число:')
    while ((sec == float(0) and sign == '/')
           or sec == 'err'):
        sec = user_input('f')
        if sec == float(0) and sign == '/':
            print('На 0 делить нельзя, повторите ввод')
        if sec == 'err':
            print('Значение введено неверно, повторите:')
    return fst, sign, sec


def arithmetic():
    """Выводит результат действия """
    fst, sign, sec = user_dialog()
    if sign is None:
        return 'До свидания'
    if sign == '+':
        print(f'{fst} {sign} {sec} = {fst+sec}')
    elif sign == '-':
        print(f'{fst} {sign} {sec} = {fst-sec}')
    elif sign == '*':
        print(f'{fst} {sign} {sec} = ' + '%0.4f'%(fst*sec))
    elif sign == '/':
        print(f'{fst} {sign} {sec} = ' + '%0.4f'%(fst/sec))
    return arithmetic()


print(arithmetic())
