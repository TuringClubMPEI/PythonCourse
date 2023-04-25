class Account:
    def __init__(self, number, name, amount):
        self.__number = number
        self.__name = name
        self.__amount = amount

    def check_amount(func):
        def wrapper(self, *args):
            if args[-1] < 0:
                print('The amount of money cannot be negative')
                return
            func(self, *args)
        return wrapper

    @check_amount
    def deposit(self, amount):
        self.__amount += amount

    @check_amount
    def withdraw(self, amount):
        if self.__amount < amount:
            print('Insufficient funds')
            return
        self.__amount -= amount

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, count):
        self.__amount = count

    @property
    def number(self):
        return self.__number


class Bank:
    def __init__(self):
        self.__accounts = []

    def find(self, number):
        result = list(filter(lambda x: x.number == number, self.__accounts))
        return result[0] if len(result) > 0 else None

    def check_account(func):
        def wrapper(self, *args):
            account = self.find(args[0])
            if account is None:
                print('An account with number {} does not exists'.format(args[0]))
                return
            func(self, account, *args[1:])
        return wrapper

    def check_amount(func):
        def wrapper(self, *args):
            if args[-1] < 0:
                print('The amount of money cannot be negative')
                return
            func(self, *args)

        return wrapper

    @check_amount
    def create_account(self, number, name, amount):
        if self.find(number) is not None:
            print('An account with number {} already exists'.format(number))
            return
        if number <= 0:
            print('Account number is a positive number')
            return
        self.__accounts.append((Account(number, name, amount)))

    @check_account
    def deposit(self, account, amount):
        account.deposit(amount)

    @check_account
    def withdraw(self, account, amount):
        account.withdraw(amount)

    @check_amount
    def transfer(self, sender, receiver, amount):
        sender_account = self.find(sender)
        if sender_account is None:
            print('An account with number {} does not exists'.format(sender))
            return
        receiver_account = self.find(receiver)
        if receiver_account is None:
            print('An account with number {} does not exists'.format(receiver))
            return
        if sender_account.amount < amount:
            print('Insufficient funds')
            return
        sender_account.amount = sender_account.amount - amount
        receiver_account.amount = receiver_account.amount + amount

    @check_account
    def get_balance(self, account):
        print('The account balance with the number {} is equal to {}'.format(account.number, account.amount))

