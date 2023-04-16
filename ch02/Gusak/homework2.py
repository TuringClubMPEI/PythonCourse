class Bank:

    NUMBERS = []
    ACCOUNTS = []

    @classmethod
    def find_in_accounts(cls, number):
        res = list(filter(lambda x: x.number == number, cls.ACCOUNTS))
        return res[0] if len(res) > 0 else None

    # sender и receiver имеют тип Account
    def transfer(self, sender, receiver, amount):
        sender.amount -= amount
        receiver.amount += amount
        return f'Сумма {amount} успешно переведена с счёта {sender} на счёт {receiver}'


class Account(Bank):

    def __init__(self, number, name, amount):
        self.name = name
        self.number = number
        self.amount = amount
        Account.NUMBERS.append(number)
        Account.ACCOUNTS.append(self)

    def deposit(self, amount):
        self.amount += amount
        return f'Сумма {amount} успешна зачислена нас счёт {self.number}'

    def withdraw(self, amount):
        self.amount -= amount
        return f'Сумма {amount} успешна снята со счёта {self.number}'

    @property
    def number(self):
        return self.number

    @number.setter
    def number(self, number):
        self.number = number

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def amount(self):
        return self.amount

    @amount.setter
    def amount(self, amount):
        self.amount = amount
