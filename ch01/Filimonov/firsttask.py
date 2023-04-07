def find(accounts, number):
    result = list(filter(lambda x: x['number'] == number, accounts))
    return result[0] if len(result) == 1 else None


def create_account(accounts, number, name, amount):
    if find(accounts, number) is not None:
        print('An account with number {} already exists'.format(number))
        return False
    if number <= 0:
        print('Account number is a positive number')
        return False
    if amount < 0:
        print('The balance cannot be negative')
        return False
    accounts.append({'number': number,
                     'name': name,
                     'amount': amount})


def deposit(accounts, number, amount):
    account = find(accounts, number)
    if account is None:
        print('An account with number {} does not exists'.format(number))
        return False
    if amount < 0:
        print('The amount of money cannot be negative')
        return False
    account['amount'] += amount


def withdraw(accounts, number, amount):
    account = find(accounts, number)
    if account is None:
        print('An account with number {} does not exists'.format(number))
        return False
    if amount < 0:
        print('The amount of money cannot be negative')
        return False
    if account['amount'] < amount:
        print('Insufficient funds')
        return False
    account['amount'] -= amount


def transfer(accounts, sender, receiver, amount):
    sender_account = find(accounts, sender)
    if sender_account is None:
        print('An account with number {} does not exists'.format(sender))
        return False
    receiver_account = find(accounts, receiver)
    if receiver_account is None:
        print('An account with number {} does not exists'.format(receiver))
        return False
    if amount < 0:
        print('The amount of money cannot be negative')
        return False
    if sender_account['amount'] < amount:
        print('Insufficient funds')
        return False
    sender_account['amount'] -= amount
    receiver_account['amount'] += amount

def get_balance(accounts, number):
    account = find(accounts, number)
    if account is None:
        print('An account with number {} does not exists'.format(number))
        return False
    print('The account balance with the number {} is equal to {}'.format(number, account['amount']))

