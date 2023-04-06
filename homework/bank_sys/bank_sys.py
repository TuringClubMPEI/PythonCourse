BANK = {'quantity_of_clients': 0}


# Function to create a bank account
#
# Input fields:
# 'name'     - full name of the bank client
# 'balance'  - how much money the client has invested in the bank
# 'accounts' - all bank accounts
#
# Output fields:
# 'number'   - bank account number


def create_account(name: str, balance: int = 0, accounts: dict = BANK):
    if name == '':  # checking client name
        # print('please enter your name')  # may be used for code without try

        raise ValueError('please enter your name')
    elif balance < 0:  # checking client investment
        # print('incorrect balance')  # may be used for code without try
        raise ValueError('incorrect balance')
    elif name in accounts:  # checked that account does not exist
        raise KeyError("user already exists")
    else:
        number = accounts['quantity_of_clients'] + 1  # create an account id
        accounts['quantity_of_clients'] = number  # create bank account
        accounts[number] = [name, balance]  # set name and first deposit to the account
        return number


# Function to add funds to the bank account
#
# Input fields:
# 'number'     - bank account number
# 'amount'     - deposit amount
# 'accounts'   - all bank accounts


def deposit(number: int, amount: float, accounts: dict = BANK):
    if number not in accounts:  # checked that account exists
        raise KeyError("user doesn't exists")
    elif amount < 0:  # check that money is the positive number
        raise ValueError("incorrect amount")
    else:
        accounts[number][1] += amount  # add money to account


# Function to withdraw money from the bank.
#
# Input fields:
# 'number'     - bank account number
# 'amount'     - withdrawal amount
# 'accounts'   - all bank accounts

def withdraw(number: int, amount: float, accounts: dict = BANK):
    if number not in accounts:  # checked that the account exists
        raise KeyError("user doesn't exists")
    elif amount < 0:  # check that money is the positive number
        raise ValueError("incorrect amount")
    elif accounts[number][1] - amount < 0:  # check
        raise ValueError("not enough money on balance")
    else:
        accounts[number][1] -= amount


# Function to create a bank account
#
# Input fields:
# 'name'     - full name of the bank client
# 'balance'  - how much money the client has invested in the bank
# 'accounts' - all bank accounts
#
# Output fields:
# 'number'   - bank account number


def transfer(sender, receiver, amount, accounts=BANK):
    if (sender not in accounts) or (receiver not in accounts):
        raise KeyError("you can't transfer to/from non-existance account")
    elif amount < 0:
        raise ValueError("inccorect amount")
    elif accounts[sender][1] - amount < 0:
        raise ValueError("not enough money on balance for transfer")
    else:
        accounts[receiver][1] += amount
        accounts[sender][1] -= amount


# Function to create a bank account
#
# Input fields:
# 'name'     - full name of the bank client
# 'balance'  - how much money the client has invested in the bank
# 'accounts' - all bank accounts
#
# Output fields:
# 'number'   - bank account number


def get_balance(number, accounts=BANK):
    if number not in accounts:
        raise KeyError("account doesn't exists")
    else:
        print("Hello {}! Thats your balance -> {}".format(accounts[number][0], accounts[number][1]))
