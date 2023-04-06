def search_account(accounts, number):
    current_account = list(filter(lambda x: x['number'] == number, accounts))
    return current_account[0] if len(current_account) == 1 else None

def create_account(accounts, number: int, name: str,amount: int):
    if search_account(accounts,number) is not None:
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
    current_account = search_account(accounts, number)
    if amount < 0:
        print('The amount of money should be a positive number!')
        return
    if current_account is None:
        print(f'A user with account number {number} does not exists!')
        return
    current_account['amount'] += amount


def withdraw(accounts, number: int, amount: int):
    current_account = search_account(accounts, number)
    if amount < 0:
        print('The amount of money should be a positive number!')
        return
    if current_account is None:
        print(f'A user with account number {number} does not exists!')
        return
    current_account['amount'] -= amount


def transfer(accounts, sender, receiver, amount):
    account_found = list(filter(lambda x: True if x['number'] in (sender, receiver) else False, accounts))
    if len(account_found) != 2:
        print('Check the account numbers! The receiver of sender does not exists')
        return
    if amount < 0:
        print('The amount of money should be a positive number!')
        return
    sender_account = list(filter(lambda x: x['number'] == sender, account_found))[0]
    receiver_account = list(filter(lambda x: x['number'] == receiver, account_found))[0]
    sender_amount = sender_account['amount']
    if sender_amount - amount <0:
        print(f'Sender has not got {amount} on his account')
        return
    sender_account['amount'] -= amount
    receiver_account['amount'] += amount


def get_balance(accounts, number):
    current_account = search_account(accounts, number)
    if current_account is None:
        print(f'A user with account number {number} does not exists!')
        return
    balance = current_account['amount']
    print(f'User with account number {number} has {balance} cu')



