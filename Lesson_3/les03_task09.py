""" 9.	Найти максимальный элемент  среди 
минимальных элементов столбцов матрицы."""
from random import randint
from functions import print_tbl

HIGH = randint(3, 50)
WIDTH = randint(3, 50)
MIN_ITEM = randint(0, 100)
MAX_ITEM = randint(0, 100)
if MIN_ITEM > MAX_ITEM:
    MIN_ITEM, MAX_ITEM = MAX_ITEM, MIN_ITEM
MATRIX = [[randint(MIN_ITEM, MAX_ITEM)
           for _ in range(HIGH)]
          for _ in range(WIDTH)]

"""В общем случае параметры матрицы нам не известны,
поэтому определяем размеры как бы вновь полученной матрицы"""
HIGH = len(MATRIX)
WIDTH = len(MATRIX[0])
MIN_IN_COLUMN = []  # хранит минимумы столбцов
ROW_OF_MIN = []  # для каждого столбца хранит
# номер строки с минимальным значением
for item in MATRIX[0]:
    MIN_IN_COLUMN.append(item)
    ROW_OF_MIN.append(0)

for string in MATRIX:
    for item in string:
        print(f"{item:4} |", end='')
    print()

for i, string in enumerate(MATRIX):
    for j, item in enumerate(string):
        if item < MIN_IN_COLUMN[j]:
            MIN_IN_COLUMN[j] = item
            ROW_OF_MIN[j] = i
print("\nМинимумы столбцов:")
print_tbl(MIN_IN_COLUMN, len(MIN_IN_COLUMN))
print("\nнаходятся в строках:")
print_tbl(ROW_OF_MIN, len(ROW_OF_MIN))

MAX_NUM = MIN_IN_COLUMN[0]
IDX_OF_MAX = 0
for i in range(len(MIN_IN_COLUMN)):
    if MIN_IN_COLUMN[i] > MAX_NUM:
        MAX_NUM = MIN_IN_COLUMN[i]
        IDX_OF_MAX = i

print(
    f"Максимальное значение среди минимумов столбцов равно {MAX_NUM}."
    f"\nОно находится в {ROW_OF_MIN[IDX_OF_MAX]} строке и {IDX_OF_MAX} столбце")
