"""Генератор массивов"""
from random import randint, uniform, random


class Array():
    """Генерация массивов"""

    def __init__(self, start_max=-100, end_max=100,
                 max_size=100, type='f'):
        """Инициализация параметров
        генерируемого массива"""
        self.start_max = start_max
        self.end_max = end_max
        self.max_size = max_size
        self.type = type

    def gen_array(self, size, start, end):
        """Генерация массива"""
        if self.type == 'f':
            array = [uniform(start, end) for _ in range(size)]
        elif self.type == 'i':
            array = [randint(start, end) for _ in range(size)]
        return array

    def rnd_len_array(self):
        """Генерация случайных параметров"""
        size = int(random() * self.max_size)
        start = int(random() * self.start_max)
        end = int(random() * self.end_max)
        rnd_array = self.gen_array(size, start, end)
        return rnd_array

    def fix_len_array(self):
        """Передача фиксированных параметров"""
        size = self.max_size
        start = self.start_max
        end = self.end_max
        fix_array = self.gen_array(size, start, end)
        return fix_array


ARRAY = Array(-50, 150, 200, 'i')
print(ARRAY.fix_len_array())
print(ARRAY.rnd_len_array())
