from ch02.Gusak.decorators import check_withdraw, check_deposit, check_transfer
from ch02.Gusak.errors import AccountNotFound, InvalidAccount


class Bank:
    def __init__(self):
        self._accounts = []

    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        self._accounts = accounts

    def find_in_accounts(self, account):
        res = list(filter(lambda x: x == account, self._accounts))
        return res[0] if len(res) > 0 else None

    # sender и receiver имеют тип Account
    @check_transfer
    def transfer(self, sender, receiver, amount):
        sender.amount -= amount
        receiver.amount += amount
        return f'Сумма {amount} успешно переведена с счёта {sender} на счёт {receiver}'


class Account:

    NUMBERS = []

    def __init__(self, number, name, amount):
        if number in Account.NUMBERS:
            raise AccountNotFound()
        if number < 0:
            raise InvalidAccount()
        self._name = name
        self._number = number
        self._amount = amount
        Account.NUMBERS.append(number)

    @check_deposit
    def deposit(self, amount):
        self._amount += amount
        return f'Сумма {amount} успешна зачислена нас счёт {self._number}'

    @check_withdraw
    def withdraw(self, amount):
        self._amount -= amount
        return f'Сумма {amount} успешна снята со счёта {self._number}'

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount
