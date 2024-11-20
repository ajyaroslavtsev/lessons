# -*- coding: utf-8 -*-


def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            print('Простое число')
        else:
            print('Составное число')
        return num
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


if __name__ == '__main__':
    result = sum_three(2, 3, 6)
    print(result)

    # Результат консоли:
    # Простое
    # 11