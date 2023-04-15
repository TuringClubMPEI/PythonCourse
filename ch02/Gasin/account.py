from decorators import *


# Банковский счет
class Account:
    # баланс денег на счете
    _balance: int
    # ФИО владельца счета
    _owner_fio: str
    # номер счета
    _number: int

    def __init__(self, number, owner_fio, balance):
        self._number = number
        self._owner_fio = owner_fio
        self._balance = balance

    @deposit_valid()
    def deposit(self, amount):
        self._balance += amount

    @withdraw_valid()
    def withdraw(self, amount):
        self._balance -= amount

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    @property
    def owner_fio(self):
        return self._owner_fio

    @owner_fio.setter
    def owner_fio(self, value):
        self._owner_fio = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value
