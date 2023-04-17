import bank_sys
import menu
import errors


def create_acc(bank):
    print('Thank you for choosing our bank')
    print('enter your name')
    name = input()
    print('enter how much money do you want to invest in our bank')
    balance = menu.get_num()
    try:
        num = bank.create_account(name=name, balance=balance)
        print('complete successful. that is you account number. don\'t forget -> ', num)
    except errors.BalanceError:
        print('creation interrupted. incorrect balance value')
    except errors.AccountError:
        print('creation interrupted. you mast enter your name')
    return bank


def auth(bank):
    print("enter your bank account number")
    try:
        bank.authorize(menu.get_num())
    except KeyError:
        print("operation interrupted. enter valid data or create new account")
        return bank, 'continue'
    return bank, 'login'


def main_menu_work(bank):
    while True:
        menu.main_menu()
        command = menu.get_num()
        # create account
        if command == 1:
            bank = create_acc(bank)
        # authorize in the bank
        elif command == 2:
            bank, stat = auth(bank)
            if stat == 'continue':
                continue
            return bank, stat
        elif command == 3:
            return bank, 'stop'
        else:
            print('retry input')


def dep(bank):
    print('enter money to put into bank')
    amount = menu.get_num()
    try:
        bank.deposit(amount=amount)
    except KeyError:
        print('deposit interrupted. account doesn\'t exist.')
    except errors.AmountError:
        print('deposit interrupted. amount value incorrect.')
    return bank


def wd(bank):
    print('enter money to withdraw')
    amount = menu.get_num()
    try:
        bank.withdraw(amount=amount)
    except KeyError:
        print('withdraw interrupted. account doesn\'t exist.')
    except errors.AmountError:
        print('withdraw interrupted. amount value incorrect.')
    except errors.BalanceError:
        print('withdraw interrupted. not enough money on balance')
    return bank


def trans(bank):
    print('enter number of receiver account')
    receiver = menu.get_num()
    print('enter amount of money for transfer')
    amount = menu.get_num()
    try:
        bank.transfer(receiver=receiver, amount=amount)
    except KeyError:
        print('transfer interrupted. account doesn\'t exist.')
    except errors.AmountError:
        print('transfer interrupted. amount value incorrect.')
    except errors.BalanceError:
        print('transfer interrupted. not enough money on balance')
    return bank


def gb(bank):
    try:
        res = bank.get_balance()
        print('You have -> {}$'.format(res))
    except KeyError:
        print('operation interrupted. enter valid account number')


def user_menu_work(bank):
    while True:
        menu.user_menu()
        command = menu.get_num()
        if command == 1:  # put money into account
            bank = dep(bank)
        elif command == 2:  # withdraw money from account
            bank = wd(bank)
        elif command == 3:  # transfer
            bank = trans(bank)
        elif command == 4:  # get balance
            gb(bank)
        elif command == 5:  # logout
            bank.logout()
            return bank, 'logout'
        else:
            print('retry input')


if __name__ == "__main__":
    Bank = bank_sys.BankSystem()
    mode = 'main'
    while True:
        if mode == 'main':
            Bank, status = main_menu_work(Bank)
            if status == 'login':
                mode = 'user'
            elif status == 'stop':
                break
        elif mode == 'user':
            Bank, status = user_menu_work(Bank)
            if status == 'logout':
                mode = 'main'
