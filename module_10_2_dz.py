import threading
from time import sleep
from random import randint
from threading import Lock

class Bank:

    def __init__(self, balance):
        super().__init__()
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        counter = 100
        self.lock.acquire()
        if self.balance >= 500 and self.lock.locked():
            self.lock.release()
        replenised = randint(50, 500)
        self.balance += replenised
        counter -= 1
        print(f"Пополнение {replenised}. Баланс{self.balance}")
        sleep(0.001)

    def take(self):
        counter = 100
        removal = randint(50, 500)
        print(f"Запрос на {removal}")
        if self.balance >= removal:
            self.balance -= removal
            counter -= 100
            print(f"Снятие: {removal}. Баланс: {self.balance}")
        else:
            print("Запрос отклонён, недостаточно средств")
            self.lock.acquire()
        sleep(0.001)

bk = Bank(500)
th1 = threading.Thread(target=Bank.deposit, args=(bk, ))
th2 = threading.Thread(target=Bank.take, args=(bk, ))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')