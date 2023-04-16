from account_errors import *


# Декоратор, говорящий о том, что перевод валидный
# В аргументах должны быть указаны:
#   bank: Bank - банк, для которого указываются счета
#   sender: Account - отправитель
#   receiver: Account - получатель
#   sum: int - сумма перевода
def transfer_valid(func):
    def _wrapper(bank, sender, receiver, amount):
        if sender is None or receiver is None:
            raise AccIsNoneError
        if bank.find_acc(sender.number) is None:
            raise AccNotFoundError(sender.number)
        if bank.find_acc(receiver.number) is None:
            raise AccNotFoundError(receiver.number)
        if sender.balance < amount:
            raise TransferAmountTooLarge(sender.number, sender.balance, amount)
        if amount <= 0:
            raise AmountInvalid(amount)

        func(bank, sender, receiver, amount)

    return _wrapper


# Декоратор, говорящий о том, что операция внесения денег на счет валидна
# В аргументах должны быть указаны:
#   account: Account - счет для внесения денег
#   sum: int - сумма перевода
def deposit_valid(func):
    def _wrapper(account, amount):
        if amount <= 0:
            raise AmountInvalid(amount)
        func(account, amount)

    return _wrapper


# Декоратор, говорящий о том, что операция снятия денег со счета валидна
# В аргументах должны быть указаны:
#   account: Account - счет для снятия денег
#   sum: int - сумма перевода
def withdraw_valid(func):
    def _wrapper(account, amount):
        if amount <= 0:
            raise AmountInvalid(amount)
        if account.balance < amount:
            raise WithdrawAmountTooLarge(account.number, account.balance, amount)

        func(account, amount)

    return _wrapper
