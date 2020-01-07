"""3. 	В массиве случайных целых 
чисел поменять местами минимальный
# и максимальный элементы."""
from functions import rnd_len_array

ARRAY = rnd_len_array(-100, 100, 15)
print(ARRAY)
MAX_I = MIN_I = 0

if len(ARRAY) > 1:
    MAX_VOL = ARRAY[0]
    MIN_VOL = ARRAY[0]
    for i, vol in enumerate(ARRAY):
        if ARRAY[i] > MAX_VOL:
            MAX_VOL = ARRAY[i]
            MAX_I = i
        elif ARRAY[i] < MIN_VOL:
            MIN_VOL = ARRAY[i]
            MIN_I = i
    ARRAY[MAX_I], ARRAY[MIN_I] = ARRAY[MIN_I], ARRAY[MAX_I]
    print(f'Минимальное и максимальное число поменяны местами:\n{ARRAY}')
else:
    print('Менять местами нечего.')
