"""5. 	В массиве найти максимальный 
отрицательный элемент.
 Вывести на экран его значение и 
 позицию (индекс) в массиве."""
from functions import rnd_len_array, print_tbl


def find_neg_elem(rnd_array):
    """Поиск максимального отрицательного
    элемента массива"""
    if len(rnd_array) != 0:
        max_el = rnd_array[0]
        max_idx = -1
        for idx, vol in enumerate(rnd_array):
            if max_el < vol < 0:
                max_el = vol
                max_idx = idx
            elif vol < 0 and max_el == rnd_array[0]:
                max_el = vol
                max_idx = idx
        return max_el, max_idx
    return None, None


RND_ARRAY = rnd_len_array(-150, 10, 100, 'f')
print('\nСгенерирован массив:\n')
print_tbl(RND_ARRAY)
MAX_EL, MAX_IDX = find_neg_elem(RND_ARRAY)
if MAX_EL is None and MAX_IDX is None:
    print('Массив пустой.')
elif MAX_EL == RND_ARRAY[0] and MAX_IDX == -1:
    print('В массиве нет отрицательных элеметов.')
else:
    print(f"\nМаксимальный отрицательный элемент массива {MAX_EL:.2f}"
          f"\nс индексом {MAX_IDX}.")
