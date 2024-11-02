# -*- coding: utf-8 -*-


first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(str_) for str_ in first_strings if len(str_)>6]
second_result = [(str_1, str_2) for str_1 in first_strings for str_2 in second_strings if len(str_1) == len(str_2)]
third_result  = {str_ : len(str_) for str_ in first_strings + second_strings if len(str_) % 2 == 0}


if __name__ == '__main__':
    print(first_result)
    print(second_result)
    print(third_result)

    # Вывод на консоль:
    '''
    [10, 8, 8]
    [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
    {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}
    '''