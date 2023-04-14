import bank_sys
import menu
import errors


def main_menu_work(bank):
    while True:
        menu.main_menu()
        command = menu.get_num()
        # create account
        if command == 1:
            print('Thank you for choosing our bank')
            print('enter your name')
            name = input()
            print('enter how much money do you want to invest in our bank')
            balance = menu.get_num()
            try:
                num = bank.create_account(name, balance)
                print('complete successful. that is you account number. don\'t forget -> ', num)
            except errors.BalanceError:
                print('creation interrupted. incorrect balance value')
                continue
            except errors.AccountError:
                print('creation interrupted. you mast enter your name')
        # authorize in the bank
        elif command == 2:
            print("enter your bank account number")
            try:
                bank.authorize(menu.get_num())
            except KeyError:
                print("operation interrupted. enter valid data or create new account")
                continue
            return bank, 'login'
        elif command == 3:
            return bank, 'stop'
        else:
            print('retry input')


def user_menu_work(bank):
    while True:
        menu.user_menu()
        command = menu.get_num()
        # put money into account
        if command == 1:
            print('enter money to put into bank')
            amount = menu.get_num()
            try:
                bank.deposit(amount)
            except KeyError:
                print('deposit interrupted. account doesn\'t exist.')
                continue
            except errors.AmountError:
                print('deposit interrupted. amount value incorrect.')
        # withdraw money from account
        elif command == 2:
            print('enter money to withdraw')
            amount = menu.get_num()
            try:
                bank.withdraw(amount)
            except KeyError:
                print('withdraw interrupted. account doesn\'t exist.')
                continue
            except errors.AmountError:
                print('withdraw interrupted. amount value incorrect.')
                continue
            except errors.BalanceError:
                print('withdraw interrupted. not enough money on balance')
        # transfer
        elif command == 3:
            print('enter number of receiver account')
            receiver = menu.get_num()
            print('enter amount of money for transfer')
            amount = menu.get_num()
            try:
                bank.transfer(receiver, amount)
            except KeyError:
                print('transfer interrupted. account doesn\'t exist.')
                continue
            except errors.AmountError:
                print('transfer interrupted. amount value incorrect.')
                continue
            except errors.BalanceError:
                print('transfer interrupted. not enough money on balance')
        # get balance
        elif command == 4:
            try:
                res = bank.get_balance()
                print('You have -> {}$'.format(res))
            except KeyError:
                print('operation interrupted. enter valid account number')
        # logout
        elif command == 5:
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
