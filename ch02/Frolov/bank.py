from decorators import *
from account import Account

class Bank:
    def __init__(self):
        self.__accounts = []

    @account_exists
    def create_account(self, number, name, amount):
        if amount < 0:
            print('You cannot operate with none positive amount of money')
            return
        current_account = Account(number, name, amount)
        self.__accounts.append(current_account)

    def search_account(self, number):
        current_account = list(filter(lambda x: x.number == number, self.__accounts))
        return current_account[0] if len(current_account) == 1 else None

    @account_not_exist
    def withdraw(self, number, amount):
        current_account = self.search_account(number)
        current_account.withdraw(amount)

    @account_not_exist
    def deposit(self, number, amount):
        current_account = self.search_account(number)
        current_account.deposit(amount)

    @validate_transfer
    def transfer(self, sender, receiver, amount):
        sender_account = self.search_account(sender)
        receiver_account = self.search_account(receiver)
        sender_account.amount -= amount
        receiver_account.amount += amount

    def get_balance(self, number):
        current_account = self.search_account(number)
        if current_account is None:
            print('Account does not exist')
            return
        return current_account.amount


# Sberbank = Bank()
# Sberbank.create_account(number=1,name='Fred',amount=1000)
# Sberbank.create_account(number=2,name='Bob',amount=400)
# Sberbank.transfer(sender=1,receiver=2,amount=10000)
# Sberbank.get_balance(1)
# Sberbank.get_balance(2)
# Sberbank.withdraw(0,10100)
# Sberbank.get_balance(1)
# Sberbank.get_balance(2)