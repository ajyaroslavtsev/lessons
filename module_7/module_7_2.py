# -*- coding: utf-8 -*-


def custom_write(file_name: str, strings: list):
    strings_positions = {}
    file = open(file_name, 'a', encoding='utf-8')
    for num_string, string in enumerate(strings, 1):
        byte_position_cursor = file.tell()
        strings_positions[(num_string, byte_position_cursor)] = string
        file.write(f'{string}\n')
    file.close()
    return strings_positions


if __name__ == '__main__':
    info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)

    # Вывод на консоль:
    '''
    ((1, 0), 'Text for tell.')
    ((2, 16), 'Используйте кодировку utf-8.')
    ((3, 66), 'Because there are 2 languages!')
    ((4, 98), 'Спасибо!')
    '''