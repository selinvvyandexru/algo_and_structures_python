"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
import random


def user_input():
    """Обрабатывает ввод пользователя"""
    try:
        vol = int(input('-->'))
    except ValueError:
        return 'err'
    else:
        return vol


def attempt_count(nmm, cnt, stg):
    """Подсчет попыток пользователя"""
    if cnt == 10:
        stg += 'Проигрыш.'
        return stg
    vol = 'err'
    print('Ваш ответ?')
    while vol == 'err':
        vol = user_input()
        if vol == 'err':
            print('Ошибка. Повторите '
                  'ввод числа (от 0 до 100).')
    if vol > nmm:
        print('Загаданное число меньше введенного.')
    elif vol < nmm:
        print('Загаданное число больше введенного.')
    else:
        stg += 'Правильно! Вы выиграли!'
        return stg
    cnt += 1
    return attempt_count(nmm, cnt, stg)


print('Загадано число от 0 до 100. Отгадайте за 10 попыток.')
print(attempt_count((random.randint(0, 100)), 0, ''))
