# -*- coding: utf-8 -*-

from multiprocessing import Pool, cpu_count
from time import time


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline().strip()
            all_data.append(line)
            if not line:
                break


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный
    start_time = time()

    for file_name in filenames:
        read_info(file_name)

    end_time = time()
    execution_time = end_time - start_time
    print(f'{execution_time} (линейный)')


    # Многопроцессный
    start_time = time()

    with Pool(processes=cpu_count()) as pool:
        pool.map(read_info, filenames)

    end_time = time()
    execution_time = end_time - start_time
    print(f'{execution_time} (многопроцессный)')