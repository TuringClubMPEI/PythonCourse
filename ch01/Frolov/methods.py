
def search_account(accounts, number):
    current_account = list(filter(lambda x: x['number'] == number, accounts))
    return current_account[0] if len(current_account) == 1 else None

def create_account(accounts, number: int, name: str,amount: int):
    if search_account(accounts,number) is not None:
        print(f'A user with account number {number} already exists!')
        return
    if amount < 0:
        print('The amount of money should be a none negative number!')
        return
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
    if current_account['amount'] < amount:
        print(f'User has not got {amount} on his account')
    current_account['amount'] -= amount


def transfer(accounts, sender, receiver, amount):
    sender_account= search_account(accounts, sender)
    receiver_account = search_account(accounts, receiver)
    if sender_account is None:
        print('Check the sender account numbers! A user with this account number does not exist')
        return
    if receiver_account is None:
        print('Check the receiver account numbers! A user with this account number does not exist')
        return
    if amount < 0:
        print('The amount of money should be a positive number!')
        return
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



