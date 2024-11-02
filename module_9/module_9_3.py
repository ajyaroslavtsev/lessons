# -*- coding: utf-8 -*-


first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(str_1) - len(str_2) for str_1, str_2 in zip(first, second) if len(str_1) != len(str_2))
second_result = (len(first[i]) == len(second[i]) for i in range(0, len(first)))


if __name__ == '__main__':
    print(list(first_result))
    print(list(second_result))
    # Вывод в консоль:
    '''
    [1, 2]
    [False, False, True]
    '''