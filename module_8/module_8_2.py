# -*- coding: utf-8 -*-


def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
    return (result, incorrect_data)

def calculate_average(numbers):
    try:
        sum_numbers, incorrect_data = personal_sum(numbers)
        return sum_numbers / (len(numbers)-incorrect_data)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


if __name__ == '__main__':
    print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

    # Вывод на консоль:
    '''
    Некорректный тип данных для подсчёта суммы - 1
    Некорректный тип данных для подсчёта суммы - ,
    Некорректный тип данных для подсчёта суммы -
    Некорректный тип данных для подсчёта суммы - 2
    Некорректный тип данных для подсчёта суммы - ,
    Некорректный тип данных для подсчёта суммы -
    Некорректный тип данных для подсчёта суммы - 3
    Результат 1: 0
    Некорректный тип данных для подсчёта суммы - Строка
    Некорректный тип данных для подсчёта суммы - Ещё Строка
    Результат 2: 2.0
    В numbers записан некорректный тип данных
    Результат 3: None
    Результат 4: 26.5
    '''
