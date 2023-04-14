def main_menu():
    print('1. create account')
    print('2. enter to the account')
    print('3. exit')


def user_menu():
    print('1. put money into account')
    print('2. withdraw money from account')
    print('3. transfer money')
    print('4. get balance')
    print('5. logout')


def get_num():
    run = True
    num = 0
    while run:
        try:
            num = int(input())
            run = False
        except ValueError:
            print('retry. please enter number')
        except KeyboardInterrupt:
            print('good bay')
    return num
