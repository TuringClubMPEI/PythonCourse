class AccNotFoundError(Exception):
    def __init__(self, *args: object):
        if args:
            self.account_number = args[0]

    def __str__(self):
        return f"Account not found with number {self.account_number}!" if self.account_number else "Account not found!"


class AccIsNoneError(Exception):
    def __init__(self, *args):
        pass

    def __str__(self):
        return "Account is none!"


class TransferAmountTooLarge(Exception):
    def __init__(self, *args):
        if args:
            self.account_number = args[0]
            self.account_balance = args[1]
            self.amount = args[2]

    def __str__(self):
        return f"{self.amount} is a too large sum to transfer for account with number {self.account_number}! " \
               f"Allowed amount is {self.account_balance}"


class AmountInvalid(Exception):
    def __init__(self, *args):
        if args:
            self.amount = args[0]

    def __str__(self):
        return f"{self.amount} is an invalid value for bank operations. Amount must be a positive number"


class WithdrawAmountTooLarge(Exception):
    def __init__(self, *args):
        if args:
            self.account_number = args[0]
            self.account_balance = args[1]
            self.amount = args[2]

    def __str__(self):
        return f"{self.amount} is a too large sum to withdraw for account with number {self.account_number}! " \
               f"Allowed amount is {self.account_balance}"
