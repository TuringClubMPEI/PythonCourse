class BalanceError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'BalanceError, {0} '.format(self.message)
        else:
            return 'BalanceError has been raised'


class AccountError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'AccountError, {0} '.format(self.message)
        else:
            return 'AccountError has been raised'


class AmountError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'AmountError, {0} '.format(self.message)
        else:
            return 'AmountError has been raised'
