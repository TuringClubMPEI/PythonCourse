import bank_sys
import menu
import errors


if __name__ == "__main__":
    while True:
        menu.print_menu()
        command = menu.get_num()
        # create account
        if command == 1:
            print('Thank you for choosing our bank')
            print('enter your name')
            name = input()
            run = True
            print('enter how much money do you want to invest in our bank')
            balance = menu.get_num()
            try:
                num = bank_sys.create_account(name, balance)
                print('complete successful. that is you account number. don\'t forget -> ', num)
            except errors.BalanceError:
                print('creation interrupted. incorrect balance value')
                continue
            except errors.AccountError:
                print('creation interrupted. you mast enter your name')
        # get balance
        elif command == 2:
            print('enter number of your account')
            num = menu.get_num()
            try:
                res = bank_sys.get_balance(num)
                print('Hello {}, nice day to see how much money you have. \n You have -> {}$'.format(res[0], res[1]))
            except KeyError:
                print('operation interrupted. enter valid account number')
        # put money into account
        elif command == 3:
            print('enter number of your account')
            num = menu.get_num()
            print('enter money to put into bank')
            amount = menu.get_num()
            try:
                bank_sys.deposit(num, amount)
            except KeyError:
                print('deposit interrupted. account doesn\'t exist.')
                continue
            except errors.AmountError:
                print('deposit interrupted. amount value incorrect.')
        # withdraw money from account
        elif command == 4:
            print('enter number of your account')
            num = menu.get_num()
            print('enter money to withdraw')
            amount = menu.get_num()
            try:
                bank_sys.withdraw(num, amount)
            except KeyError:
                print('withdraw interrupted. account doesn\'t exist.')
                continue
            except errors.AmountError:
                print('withdraw interrupted. amount value incorrect.')
                continue
            except errors.BalanceError:
                print('withdraw interrupted. not enough money on balance')
        # transfer money
        elif command == 5:
            print('enter number of your account')
            sender = menu.get_num()
            print('enter number of receiver account')
            receiver = menu.get_num()
            print('enter amount of money for transfer')
            amount = menu.get_num()
            try:
                bank_sys.transfer(sender, receiver, amount)
            except KeyError:
                print('withdraw interrupted. account doesn\'t exist.')
                continue
            except errors.AmountError:
                print('withdraw interrupted. amount value incorrect.')
                continue
            except errors.BalanceError:
                print('withdraw interrupted. not enough money on balance')
        # exit bank
        elif command == 6:
            break
        else:
            print('retry input')
