"""Генератор массивов"""
from random import randint, uniform, random


def gen_array(start, end, size, el_type='x'):
    """Генерация массива"""
    if start > end:
        start, end = end, start
    if el_type == 'f':
        array = [uniform(start, end) for _ in range(size)]
    elif el_type == 'i':
        array = [randint(start, end) for _ in range(size)]
    else:
        print('Не определен тип данных в массиве.')
        return None
    return array


def rnd_len_array(start_max, end_max, max_size, el_type='i'):
    """Генерация случайных параметров"""
    size = int(random() * max_size)
    start = int(random() * start_max)
    end = int(random() * end_max)
    rnd_array = gen_array(start, end, size, el_type)
    return rnd_array


def fix_len_array(start, end, size, el_type='i'):
    """Передача фиксированных параметров"""
    fix_array = gen_array(start, end, size, el_type)
    return fix_array


def print_tbl(array, elem_in_str=10, start=0):
    """Выводит на экран сгенерированный массив
    в виде таблицы"""
    array_len = len(array)
    if array_len > 0:
        if str(type(array[0])) == "<class 'float'>":
            # el1 = str('{:>8}')  # игрался для себя как можно формировать
            # el2 = str('%0.2f')  # параметры вывода программно
            elf = '8.2f'
        elif str(type(array[0])) == "<class 'int'>":
            # el1 = str('{:>5}')
            # el2 = str('%5.0d')
            spam = len(str(max(array)))
            egg = len(str(min(array)))
            if spam > egg:
                elf = str(spam + 2)
            else:
                elf = str(egg + 2)
        while start < array_len != 0:
            end = start + elem_in_str
            if end > array_len:
                end = array_len
            for idx in range(start, end):
                print(f"{array[idx]:{elf}}|", end='')
                # print((el1.format(el2 % array[idx]) + ' |'), end=' ')
            start = end
            print()
    else:
        print('')
