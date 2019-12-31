"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


def num_reverse(num, ren):
    """Производит разворот числа"""
    if num == 0:
        return ren
    ren += str(num % 10)
    num = num // 10
    return num_reverse(num, ren)


try:
    NUM = int(input('Введите целое многозначное число: '))
except ValueError:
    print('Ошибка. Вводите данные внимательнее.')
else:
    print(num_reverse(NUM, ''))
