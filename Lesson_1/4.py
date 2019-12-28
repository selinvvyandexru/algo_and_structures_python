"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""
import random


def user_input(dtp):
    """Принимает значения границ диапазона,
    производит проверку и преобразование к нужному типу"""
    sta = input('Введите начало диапазона: ')
    fin = input('Введите конец диапазона:  ')
    try:
        if dtp == 'i':
            sta = int(sta)
            fin = int(fin)
        elif dtp == 'f':
            if ',' in sta:
                sta = sta.replace(',', '.')
            if ',' in fin:
                fin = fin.replace(',', '.')
            sta = float(sta)
            fin = float(fin)
        elif dtp == 's':
            sta = sta.lower()
            fin = fin.lower()
            sta = ord(sta)
            fin = ord(fin)
            if 97 <= sta <= 122 or (
                    97 <= fin <= 122):
                pass
            else:
                print('Нужно вводить символы ЛАТИНСКОГО алфавита')
                return None
        else:
            print('Тип данных не определён.')
            return None
        if sta > fin:
            sta, fin = fin, sta
        return sta, fin
    except (ValueError, TypeError):
        print('Одно из значений введено неверно')


try:
    print('Генерация случайного целого числа из заданного диапазона')
    DTP = 'i'
    STA, FIN = user_input(DTP)
    print(f'Сгенерировано чмсло: {random.randint(STA, FIN)}')
    print('\nГенерация случайного вещественного числа')
    DTP = 'f'
    STA, FIN = user_input(DTP)
    print(f'Сгенерировано чмсло: {random.uniform(STA, FIN)}')
    print('\nГенерация случайного символа латинского алфавита')
    DTP = 's'
    STA, FIN = user_input(DTP)
    print(f'Сгенерирован символ: {chr(random.randint(STA, FIN))}')
except (TypeError, ValueError):
    print('При работе произошла ошибка')
