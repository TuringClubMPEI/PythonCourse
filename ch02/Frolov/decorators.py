
def validate_amount(func):
    def wrapper(account, amount):
        if amount <= 0:
            print('You cannot operate with none positive amount of money')
            return
        func(account, amount)
    return wrapper


def validate_account(func):
    def wrapper(bank, number):
        current_account = bank.search_account(number)
        if current_account is None:
            print('Account not found')
            return
        func(bank, number)
    return wrapper


def account_exists(func):
    def wrapper(bank, **kwargs):
        current_account = bank.search_account(kwargs.get('number'))
        if current_account is not None:
            print('Account already exists')
            return
        func(bank, **kwargs)
    return wrapper


def account_not_exist(func):
    def wrapper(bank, number, amount):
        current_account = bank.search_account(number)
        if current_account is None:
            print('Account does not exist')
            return
        func(bank, number, amount)
    return wrapper


def validate_transfer(func):
    def wrapper(bank, sender, receiver, amount):
        current_sender = bank.search_account(sender)
        current_receiver = bank.search_account(receiver)
        if current_sender is None:
            print('Senders account does not exist')
            return
        if current_receiver is None:
            print('Receivers account does not exist')
            return
        if current_sender.amount - amount < 0:
            print('Insufficient Funds')
            return
        func(bank,sender, receiver, amount)
    return wrapper
