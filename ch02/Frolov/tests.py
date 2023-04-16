from bank import Bank

def test_1():
    print('-'*100)
    print('Test 1')
    print('Test to check the correctness of all methods, in the case when the user does not exist')
    print('-' * 100)
    bank = Bank()
    bank.create_account(number= 1, name='Fred', amount=123)
    bank.deposit(2, 100)
    bank.withdraw(2, 20)
    bank.transfer(2, 3, 10)
    bank.transfer(1, 3, 10)
    bank.transfer(3, 1, 10)
    bank.get_balance(2)
    print(bank._Bank__accounts[0])
    print()


def test_2():
    print('-'*100)
    print('Test 2')
    print('A test to verify the correctness of the creation and transfer methods,\n'
          'in the case of creating a user with an existing number and transferring money to a non-existent user')
    print('-' * 100)
    bank = Bank()
    bank.create_account(number=1, name='Fred', amount=500)
    bank.create_account(number=1,name='Bob', amount=200)
    bank.transfer(1, 2, 10)
    bank.transfer(2,1,10)
    print(bank._Bank__accounts[0])
    print()


def test_3():
    print('-'*100)
    print('Test 3')
    print('A test to verify the correctness of the all methods,\n'
          'in the case of creating a user with negative balance or transferring negative amount of money'
          'or transferring the amount of money user does not have on his account')
    print('-' * 100)
    bank = Bank()
    bank.create_account(number=1, name='Fred', amount=-500)
    bank.create_account(number=1, name='Bob', amount=500)
    bank.create_account(number=2, name='Fred', amount=600)
    bank.deposit(1,-100)
    bank.withdraw(1, -100)
    bank.transfer(1, 2, -100)
    bank.transfer(1,2,1000)
    bank.transfer(2, 1, 900)
    print(bank._Bank__accounts[0])
    print(bank._Bank__accounts[1])
    print()



def test_4():
    print('-'*100)
    print('Test 4')
    print('A test to verify the correctness of the all methods,\n'
          'using normal cases')
    print('-' * 100)
    bank = Bank()
    bank.create_account(number=1, name='Bob', amount=500)
    bank.create_account(number=2, name='Fred', amount=600)
    bank.deposit(1,100)
    bank.withdraw(2, 200)
    bank.transfer(1, 2, 400)
    bank.get_balance(1)
    bank.get_balance(2)
    print(bank._Bank__accounts[0])
    print(bank._Bank__accounts[1])
    print()




