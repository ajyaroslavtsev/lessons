# -*- coding: utf-8 -*-

from random import choice


# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))


# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for elem in data_set:
                file.write(f'{str(elem)}\n')
    return write_everything


# Метод __call__:
class MysticBall:
    def __init__(self, *words) -> None:
        self.words = words

    def __call__(self):
        return choice(self.words)


if __name__ == '__main__':
    # [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
    print(result)
    
    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())
    print(first_ball())
    print(first_ball())





