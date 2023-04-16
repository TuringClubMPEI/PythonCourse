from decorators import *

class Account:
    def __init__(self, number, name, amount):
        self.__number = number
        self.__name = name
        self.__amount = amount

    def __str__(self):
        return f'{self.__number} | {self.__name} | {self.__amount}'

    @validate_amount
    def deposit(self, amount):
        self.__amount += amount

    @validate_amount
    def withdraw(self, amount):
        if self.__amount - amount <0:
            print('Insufficient Funds')
            return False
        self.__amount -= amount

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, input_amount):
        self.__amount = input_amount

    @property
    def name(self):
        return self.__name

    @property
    def number(self):
        return self.__number







# fred = Account(1,'fred',1000)
# fred.deposit(-100)
# print(fred.amount)
# fred.deposit(100)
# print(fred.amount)
# fred.withdraw(-1000)
# print(fred.amount)
# fred.withdraw(1200)
# print(fred.amount)
# fred.withdraw(200)
# print(fred.amount)

