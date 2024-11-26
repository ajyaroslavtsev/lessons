# -*- coding: utf-8 -*-


from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self) -> None:
        self.balance = 0
        self.lock = Lock()
        self.num_of_transactions = 100

    def deposit(self):
        for _ in range(self.num_of_transactions):
            random_num = randint(50, 500)
            self.balance += random_num
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {random_num}. Баланс: {self.balance}')                
            sleep(0.001)

    def take(self):
        for _ in range(self.num_of_transactions):
            random_num = randint(50, 500)
            print(f'Запрос на {random_num}')
            if self.balance >= random_num:
                self.balance -= random_num
                print(f'Снятие: {random_num}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


if __name__ == '__main__':
    bk = Bank()

    # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
    th1 = Thread(target=Bank.deposit, args=(bk,))
    th2 = Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')