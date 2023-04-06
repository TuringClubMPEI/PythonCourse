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


def create_account(name: str, balance: int = 0, accounts=BANK):
    if name == '':  # checking client name
        # print('please enter your name')  # may be used for code without try
        raise ValueError('please enter your name')
    elif balance < 0:  # checking client investment
        # print('incorrect balance')  # may be used for code without try
        raise ValueError('incorrect balance')
    elif name in accounts:
        raise KeyError("user already exists")
    else:
        number = accounts['quantity_of_clients'] + 1  # create an account id
        accounts['quantity_of_clients'] = number
        accounts[number] = [name, balance]


def deposit(number, amount, accounts=BANK):
    if number not in accounts:
        raise KeyError("user doesn't exists")
    elif amount < 0:
        raise ValueError("inccorect amount")
    else:
        accounts[number][1] += amount


def withdraw(number, amount, accounts=BANK):
    if number not in accounts:
        raise KeyError("user doesn't exists")
    elif amount < 0:
        raise ValueError("inccorect amount")
    elif accounts[number][1] - amount < 0:
        raise ValueError("not enough money on balance")
    else:
        accounts[number][1] -= amount

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


def get_balance(number, accounts=BANK):
    if number not in accounts:
        raise KeyError("account doesn't exists")
    else:
        print("Hello {}! Thats your balance -> {}".format(accounts[number][0], accounts[number][1]))
