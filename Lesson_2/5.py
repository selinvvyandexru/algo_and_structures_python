"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def ascii_print(nus, nue, std):
    """Формирует таблицу кодов
    в заданном диапазоне"""
    if nus >= nue:
        return std
    nup = nus + 10
    if nup > nue + 1:
        nup = nue + 1
    stc = ''
    while nus < nup:
        stc += ('{:>4}'.format(str(nus)) +
                '{:>4}'.format(chr(nus)) + ' |')
        nus += 1
    std += '\n' + stc
    return ascii_print(nus, nue, std)


print(ascii_print(32, 127, ''))
