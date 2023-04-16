from account import Account
from decorators import *


# Банк
class Bank:
    # Список открытых счетов банка
    _accounts: list

    def __init__(self):
        self._accounts = []

        # Перевод денег со счета на счет

    @transfer_valid
    def transfer(self, sender: Account, receiver: Account, amount: int):
        sender.balance -= amount
        receiver.balance += amount

    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        self._accounts = accounts

    def find_acc(self, number):
        try:
            return next(filter(lambda acc: acc.number == number, self._accounts))
        except StopIteration:
            return None
