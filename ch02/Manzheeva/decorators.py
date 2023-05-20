def number_checker(func):
    def wrapper(account, number, name, balance):
        if number<0:
            print("Ошибка, номер счета не может быть отрицательным")
        if account.account_exists(number):
            print('Ошибка, аккаунт с таким номером уже существует')
            return
        if balance<0:
            print ('Ошибка, Баланс не может быть отрицательным')
            return
        func(account, number, name, balance)
    return wrapper


def  transfer_validation(func):
    def wrapper(account, sender, receiver, amount):
        if sender.balance<amount:
            print("Ошибка, недостаточно средств на счете")
            return
        if amount < 0:
            print('Ошибка, cумма не может быть отрицательной')
            return
        func(account, sender, receiver, amount)
    return wrapper


def withdraw_validation(func):
    def wrapper(account, amount):
        if account.balance < amount:
            print("Ошибка, недостаточно средств на счете")
            return
        if amount < 0:
            print('Ошибка, cумма не может быть отрицательной')
            return
        func(account, amount)
    return wrapper

def deposit_validation(func):
    def wrapper(account, amount):
        if amount < 0:
            print('Ошибка, cумма не может быть отрицательной')
            return
        func(account, amount)
    return wrapper
