"""
6.	В  одномерном массиве найти сумму 
элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный 
элементы в сумму не включать.
"""
from functions import rnd_len_array, print_tbl


def find_min_max(array, min_count=0, max_count=0):
    """Ищет минимальные и максимальные
    значения в массиве, а также считает сколько
    раз эти значения встречаются"""
    try:
        min_vol = array[0]
        max_vol = array[0]
    except IndexError:
        print('Пустой массив.')
        return 0, 0, 0, 0
    else:
        for vol in array:
            if vol == max_vol:
                max_count += 1
            if vol == min_vol:
                min_count += 1
            elif vol > max_vol:
                max_vol = vol
                max_count = 1
            elif vol < min_vol:
                min_vol = vol
                min_count = 1
        if min_vol == max_vol:
            max_count = 0
        return min_vol, max_vol, min_count, max_count


def find_sorted_min_max(array, min_count=0, max_count=0):
    """Ищет минимальные и максимальные
        значения в отсортированном
        массиве, а также считает сколько
        раз эти значения встречаются"""
    try:
        array = sorted(array)
        min_vol = array[0]
        max_vol = array[-1]
        array_len = len(array)
    except IndexError:
        print('Пустой массив')
        return 0, 0, 0, 0
    else:
        for idx in range(array_len):
            rev_idx = array_len - idx - 1
            if min_vol == array[idx]:
                min_count += 1
            if max_vol == array[rev_idx]:
                max_count += 1
            if (min_vol != array[idx]
                    and max_vol != array[rev_idx]):
                return min_vol, max_vol, min_count, max_count
        if min_vol == max_vol:
            max_count = 0
        return min_vol, max_vol, min_count, max_count


def sum_array_elements(array, find_method, array_sum=0):
    """Суммирует элементы массива,
    исключая минимальные и максимальные
    значения"""
    if find_method == 1:
        min_vol, max_vol, min_count, max_count = find_min_max(array)
    else:
        min_vol, max_vol, min_count, max_count = find_sorted_min_max(array)
    for vol in array:
        array_sum += vol
    array_sum -= ((min_vol * min_count) + (max_vol * max_count))
    return array_sum


ARRAY = rnd_len_array(-50, 50, 100, 'f')
print('\nСгенерирован массив:\n')
print_tbl(ARRAY)
print(f'\nСумма элементов массива без пограничных значений: ')
print(f"\n- поиск границ без сортировки: "
      f"{sum_array_elements(ARRAY, 1):.2f}")
print(f'\n- поиск границ в отсортированном массиве: '
      f"{sum_array_elements(ARRAY, 2):.2f}")
