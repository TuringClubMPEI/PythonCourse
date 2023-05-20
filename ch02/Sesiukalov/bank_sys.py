import errors
import getpass

"""
Module that implemented little banking application. Enjoy working.
"""


def check_param(func):
    def _wrapper(*args, **kwargs):
        if kwargs.get("balance", 1) < 0:
            raise errors.BalanceError("incorrect balance")
        elif kwargs.get("amount", 1) < 0:
            raise errors.AmountError("incorrect amount")
        elif kwargs.get("name", '0') == '':  # checking client name
            raise errors.AccountError('please enter your name')
        return func(*args, **kwargs)
    return _wrapper


class BankSystem:
    """
    Bank system class

    Note:
        Implements a banking application prototype. You can create an account,
        put money on it, transfer it to another account. There is support for passwords.

    :except AmountError:
    :except BalanceError:
    :except AccountError:
    :except PasswordError:
    """

    class Account:
        @check_param
        def __init__(self, name: str, number: int, password: int, balance: int = 0):
            self._name = name
            self._balance = balance
            self._number = number
            self._password = password

        @property
        def number(self):
            return self._number

        @property
        def balance(self):
            return self._balance

        @balance.setter
        @check_param
        def balance(self, amount: int):
            """
            Function to add funds to the bank account or withdraw them

            :param amount:     - deposit amount
            """
            self._balance = amount  # add money to account

        @property
        def name(self):
            return self._name

        @name.setter
        @check_param
        def name(self, name: str):
            self._name = name
            
        @property
        def password(self):
            return self._password
        
        @password.setter
        def password(self, password):
            self._password = password

    __ONLINE = -1

    def authorize(self, num: int) -> None:
        """
        Function to authorized in bank system

        :param num: - bank account number
        :except KeyError:  you can't authorize to non-existence account
        """
        i = BankSystem.find_account(self, num)
        if i is None:
            raise KeyError("you can't transfer to/from non-existence account")
        password = hash(getpass.getpass("enter your password"))
        if self._bank[i].password == password:
            BankSystem.__ONLINE = i

    @staticmethod
    def logout():
        BankSystem.__ONLINE = -1

    def __init__(self):
        """Function to start work with bank system"""
        self._bank: list[BankSystem.Account] = []
        self._quantity_of_clients = 0

    @check_param
    def create_account(self, name: str, balance: int = 0):
        """
        Function to create a bank account

        :param name:       - full name of the bank client
        :param balance:    - how much money the client has invested in the bank
        """
        number = self._quantity_of_clients + 1  # create an account id
        self._quantity_of_clients = number
        password = hash(getpass.getpass("please, enter password to your account"))
        acc = BankSystem.Account(name, number, password, balance)  # create bank account
        self._bank += [acc]  # add account to bank system
        return number

    def find_account(self, number: int):
        """
        Function to find bank account in system

        :param number: - number for search bank account
        """
        for i in range(self._quantity_of_clients):
            if self._bank[i].number == number:
                return i
        return None

    @check_param
    def transfer(self, receiver: int, amount: int):
        """
        Function to transfer money to another bank account

        :param amount: - money fo transfer
        :param receiver: - account number of receiver
        """
        if i := BankSystem.find_account(self, receiver) is None:  # checked that receiver exists in bank system
            raise KeyError("you can't transfer to/from non-existence account")
        if self._bank[BankSystem.__ONLINE].balance - amount < 0:  # checked that sender has money for withdraw
            raise errors.BalanceError("not enough money on balance for transfer")
        self._bank[i].balance += amount  # add money to receiver
        self._bank[BankSystem.__ONLINE].balance -= amount  # withdraw money from account

    def deposit(self, amount):
        self._bank[BankSystem.__ONLINE].balance += amount

    @check_param
    def withdraw(self, amount):
        if self.get_balance() - amount < 0:
            raise errors.BalanceError('not enough money for withdraw')
        self._bank[BankSystem.__ONLINE].balance -= amount

    def get_balance(self):
        return self._bank[BankSystem.__ONLINE].balance
