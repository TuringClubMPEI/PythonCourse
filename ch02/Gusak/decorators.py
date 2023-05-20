from .errors import AccountNotFound, AmountLessZero, InsufficientFunds


def check_deposit(func):
    def _wrapper(cls, amount):
        if amount <= 0:
            raise AmountLessZero()
        return func(cls, amount)
    return _wrapper


def check_withdraw(func):
    def _wrapper(cls, amount):
        if amount <= 0:
            raise AmountLessZero()
        if cls.amount - amount < 0:
            raise InsufficientFunds()
        return func(cls, amount)
    return _wrapper


def check_transfer(func):
    def _wrapper(bank, sender, receiver, amount):
        if not sender or not receiver or not bank.find_in_accounts(sender) or \
                not bank.find_in_accounts(receiver):
            raise AccountNotFound()
        if amount <= 0:
            raise AmountLessZero()
        if sender.amount - amount < 0:
            raise InsufficientFunds()
        return func(bank, sender, receiver, amount)
    return _wrapper
