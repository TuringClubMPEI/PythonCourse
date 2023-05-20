class AmountLessZero(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Сумма меньше нуля'


class InsufficientFunds(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'На счёте недостаточно средств'


class AccountNotFound(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Счёт не найден'


class AccountAlreadyExist(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Счёт с таким номером уже существует'


class InvalidAccount(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Некорректный номер счёта'
