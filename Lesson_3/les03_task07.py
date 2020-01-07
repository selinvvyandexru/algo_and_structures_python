"""
7.	В одномерном  массиве целых чисел 
определить два наименьших элемента.
Они могут быть как равны между собой 
(оба являться минимальными),
 так и различаться.
"""
from functions import rnd_len_array, print_tbl

ARRAY = rnd_len_array(-100, 100, 70)
print('\nСгенерирован массив:\n')
print_tbl(ARRAY)
try:
    MIN1 = MIN2 = ARRAY[0]
except IndexError:
    print('Пустой массив.')
else:
    for vol in ARRAY:
        if vol < MIN1:
            if MIN1 < MIN2:
                MIN2 = MIN1
            MIN1 = vol
        elif vol < MIN2:
            MIN2 = vol
    print(
        f'\nДва минимальных элемента равны {MIN1}'
        if MIN1 == MIN2 else
        f'\nМинимальные элементы равны {MIN1} и {MIN2}')
