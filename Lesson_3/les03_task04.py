"""# 4. 	Определить, какое число в 
массиве встречается чаще всего."""
from functions import rnd_len_array, print_tbl


def count_interm_array(array):
    """Находит часто повторяющееся число
    с помощью промежуточных массивов"""
    repeat_array = []
    count_array = []
    max_count = 0
    idx_max = 0
    idx = 0
    for item in array:
        if item in repeat_array:
            idx = repeat_array.index(item)
            count_array[idx] += 1
        else:
            repeat_array.append(item)
            count_array.append(1)
        if count_array[idx] >= max_count:
            max_count = count_array[idx]
            idx_max = idx
    return repeat_array[idx_max], count_array[idx_max]


def count_sorted_array(array):
    """Производит подсчет в отсортированном массиве"""
    array = sorted(array)
    print_tbl(array)
    num = array[0]
    max_num = array[0]
    max_count = 0
    tmp_count = 0
    for i in array:
        if i == num:
            tmp_count += 1
            if tmp_count > max_count:
                max_count = tmp_count
                max_num = num
        else:
            tmp_count = 1
            num = i
    return max_num, max_count


ARRAY = rnd_len_array(0, 20, 100)
print('\nСгенерирован массив:\n')
print_tbl(ARRAY)

if len(ARRAY) > 0:
    print('\nПодсчет через промежуточные массивы.')
    NUM_COUNT_ARRAY, VOL_COUNT_ARRAY = count_interm_array(ARRAY)
    print(f'Чаще всего встречается число {NUM_COUNT_ARRAY}'
          f'\n встречается {VOL_COUNT_ARRAY} раз(-а)'
          if VOL_COUNT_ARRAY != 1 else
          'Все элементы массива уникальны.')

    print('\nПодсчет в упорядоченном массиве.')
    NUM_COUNT_ARRAY, VOL_COUNT_ARRAY = count_sorted_array(ARRAY)
    print(f'Чаще всего встречается число {NUM_COUNT_ARRAY}'
          f'\n встречается {VOL_COUNT_ARRAY} раз(-а)'
          if VOL_COUNT_ARRAY != 1 else
          'Все элементы массива уникальны.')
else:
    print('Пустой массив.')
