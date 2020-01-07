"""
8.	Матрица 5x4  заполняется вводом с клавиатуры кроме 
последних элементов строк.
Программа должна вычислять сумму 
введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
WIDTH = 4
MATRIX = [[0 for _ in range(WIDTH)] for _ in range(WIDTH + 1)]

for i in range(WIDTH + 1):
    sum_line = 0
    for j in range(WIDTH - 1):
        try:
            MATRIX[i][j] = int(input('Введите целое число: '))
        except ValueError:
            print('ОШИБКА.Внимательно вводите значения.'
                  '\nОставлен 0.')
        else:
            sum_line += MATRIX[i][j]
    MATRIX[i][j + 1] = sum_line

print(*MATRIX, sep='\n')
