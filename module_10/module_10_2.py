# -*- coding: utf-8 -*-


from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power) -> None:
        super().__init__()
        self.name = name
        self.power = power
        self.number_enemy = 100
        self.number_of_day = 0
        self.start()

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.number_enemy > 0:
            self.number_enemy -= self.power
            sleep(1)
            self.number_of_day += 1
            print(f"{self.name} сражается {self.number_of_day} день(дня).., осталось {self.number_enemy} воинов.")
        print(f"{self.name} одержал победу спустя {self.number_of_day} дней(дня)!")


if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    first_knight.join()
    second_knight.join()

    print('Все битвы закончились!')

    # Вывод на консоль:
    '''
    Sir Lancelot, на нас напали!
    Sir Lancelot, сражается 1 день(дня)..., осталось 90 воинов.
    Sir Galahad, на нас напали!
    Sir Galahad, сражается 1 день(дня)..., осталось 80 воинов.
    Sir Galahad, сражается 2 день(дня)..., осталось 60 воинов.
    Sir Lancelot, сражается 2 день(дня)..., осталось 80 воинов.
    Sir Lancelot, сражается 3 день(дня)..., осталось 70 воинов.
    Sir Galahad, сражается 3 день(дня)..., осталось 40 воинов.
    Sir Lancelot, сражается 4 день(дня)..., осталось 60 воинов.
    Sir Galahad, сражается 4 день(дня)..., осталось 20 воинов.
    Sir Galahad, сражается 5 день(дня)..., осталось 0 воинов.
    Sir Lancelot, сражается 5 день(дня)..., осталось 50 воинов.
    Sir Lancelot, сражается 6 день(дня)..., осталось 40 воинов.
    Sir Galahad одержал победу спустя 5 дней(дня)!
    Sir Lancelot, сражается 7 день(дня)..., осталось 30 воинов.
    Sir Lancelot, сражается 8 день(дня)..., осталось 20 воинов.
    Sir Lancelot, сражается 9 день(дня)..., осталось 10 воинов.
    Sir Lancelot, сражается 10 день(дня)..., осталось 0 воинов.
    Sir Lancelot одержал победу спустя 10 дней(дня)!
    Все битвы закончились!
    '''