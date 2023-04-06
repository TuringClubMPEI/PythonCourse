
def create_account(accounts, number: int, name: str,amount: int):
    if any([True for account in accounts if account['number'] == number]):
        print(f'A user with account number {number} already exists!')
    elif amount < 0:
        print('The amount of money should be a none negative number!')
    else:
        new_account = {
            'number': number,
            'name': name,
            'amount': amount,
        }
        accounts.append(new_account)


def deposit(accounts, number: int, amount: int):
    current_account = list(filter(lambda x: True if x['number'] == number else False, accounts))
    if amount < 0:
        print('The amount of money should be a positive number!')
    elif len(current_account) == 0:
        print(f'A user with account number {number} does not exists!')
    else:
        current_account[0]['amount'] += amount


def withdraw(accounts, number: int, amount: int):
    current_account = list(filter(lambda x: True if x['number'] == number else False, accounts))
    if amount < 0:
        print('The amount of money should be a positive number!')
    elif len(current_account) == 0:
        print(f'A user with account number {number} does not exists!')
    else:
        current_account[0]['amount'] -= amount


def transfer(accounts, sender, receiver, amount):
    account_found = list(filter(lambda x: True if x['number'] in (sender, receiver) else False, accounts))
    if len(account_found) != 2:
        print('Check the account numbers! The receiver of sender does not exists')
    elif amount < 0:
        print('The amount of money should be a positive number!')
    else:
        sender_account = list(filter(lambda x: True if x['number'] == sender else False, account_found))[0]
        receiver_account = list(filter(lambda x: True if x['number'] == receiver else False, account_found))[0]
        sender_amount = sender_account['amount']
        if sender_amount - amount >=0:
            sender_account['amount'] -= amount
            receiver_account['amount'] += amount
        else:
            print(f'Sender has not got {amount} on his account')


def get_balance(accounts, number):
    current_account = list(filter(lambda x: True if x['number'] == number else False, accounts))
    if len(current_account) != 1:
        print(f'A user with account number {number} does not exists!')
    else:
        balance = current_account[0]['amount']
        print(f'User with account number {number} has {balance} cu')



