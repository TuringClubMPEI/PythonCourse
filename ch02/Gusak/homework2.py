def check_if_amount_more_zero(func):
    def _wrapper(*args):
        amount = args[-1]
        if amount <= 0:
            print(f'Невозможно открыть счёт с начальной суммой {amount}')
            return None
        return func(*args)
    return _wrapper


def check_if_number_not_in_accounts(func):
    def _wrapper(*args):
        number = args[1]
        class_el = args[0]
        if class_el.find_in_accounts(number):
            print(f'Невозможно открыть счёт с номером счёта {number}')
            return None
        return func(*args)
    return _wrapper


def check_enough_amount(func):
    def _wrapper(*args):
        amount_on_account = args[0].amount
        amount = args[-1]
        if amount_on_account - amount >= 0:
            return func(*args)
        print('На счёте недостатоно средств')
        return None
    return _wrapper


class Bank:

    NUMBERS = []
    ACCOUNTS = []

    @classmethod
    def find_in_accounts(cls, number):
        res = list(filter(lambda x: x.number == number, cls.ACCOUNTS))
        return res[0] if len(res) > 0 else None

    @check_if_amount_more_zero
    def transfer(self, sender, receiver, amount):
        sender_data = Bank.find_in_accounts(sender)
        receiver_data = Bank.find_in_accounts(receiver)
        if (not sender_data) and (not receiver_data):
            return f'Счёта {sender} и {receiver} не нашлись'
        if not sender_data:
            return f'Счёта {sender} не нашлось'
        if not receiver_data:
            return f'Счёта {receiver} не нашлось'
        if sender_data.amount < amount:
            return f'На счёте {sender} недостатоно средств'

        sender_data.amount -= amount
        receiver_data.amount += amount
        return f'Сумма {amount} успешно переведена с счёта {sender} на счёт {receiver}'

    @staticmethod
    def get_balance(number):
        data = Bank.find_in_accounts(number)
        if data:
            return data.amount
        return 'Счёта не нашлось'


class Account(Bank):

    @check_if_amount_more_zero
    @check_if_number_not_in_accounts
    def __init__(self, number, name, amount):
        self.name = name
        self.number = number
        self.amount = amount
        Account.NUMBERS.append(number)
        Account.ACCOUNTS.append(self)

    @check_if_amount_more_zero
    def deposit(self, amount):
        self.amount += amount
        return f'Сумма {amount} успешна зачислена нас счёт {self.number}'

    @check_if_amount_more_zero
    @check_enough_amount
    def withdraw(self, amount):
        self.amount -= amount
        return f'Сумма {amount} успешна снята со счёта {self.number}'

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    property(get_number, set_number)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    property(get_name, set_name)

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    property(get_amount, set_amount)
