def print_menu():
    print('1. create account')
    print('2. get balance')
    print('3. put money into account')
    print('4. withdraw money from account')
    print('5. transfer money')
    print('6. exit')


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
