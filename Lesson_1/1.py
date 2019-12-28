""" 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."""

NUMBER = input('Введите трехзначное целое число: ')

try:
    if len(NUMBER) == 3:
        NUMBER = int(NUMBER)
        A = NUMBER // 100
        B = NUMBER % 100 // 10
        C = NUMBER % 10
        SMM = A + B + C
        MUL = A * B * C
        print(f'Сумма цифр введенного числа - {SMM}')
        print(f'Произведение цифр введенного числа - {MUL}')
    else:
        print('Данные введены неверно.')
except ValueError:
    print('Вы ввели неверные данные.')
