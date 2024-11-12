# -*- coding: utf-8 -*-


def all_variants(text):
    n = len(text)
    for i in range(1, n + 1):
        for j in range(n - i + 1):
            yield text[j: j + i]


if __name__ == '__main__':
    a = all_variants("abc")
    for i in a:
        print(i)
    
    # Вывод на консоль:
    """ 
    a
    b
    c
    ab
    bc
    abc
    """
