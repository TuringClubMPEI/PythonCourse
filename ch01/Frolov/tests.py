from methods import *


def test_1():
    print('-'*100)
    print('Test 1')
    print('Test to check the correctness of all methods, in the case when the user does not exist')
    print('-' * 100)
    accounts = []
    create_account(accounts, 1, 'Fred', 123)
    deposit(accounts, 2, 100)
    withdraw(accounts, 2, 20)
    transfer(accounts, 2, 3, 10)
    get_balance(accounts, 2)
    print()


def test_2():
    print('-'*100)
    print('Test 2')
    print('A test to verify the correctness of the creation and transfer methods,\n'
          'in the case of creating a user with an existing number and transferring money to a non-existent user')
    print('-' * 100)
    accounts = []
    create_account(accounts, 1, 'Fred', 500)
    create_account(accounts,1,'Bob', 200)
    transfer(accounts, 1, 2, 10)
    transfer(accounts, 2,1,10)
    print()


def test_3():
    print('-'*100)
    print('Test 3')
    print('A test to verify the correctness of the all methods,\n'
          'in the case of creating a user with negative balance or transferring negative amount of money'
          'or transferring the amount of money user does not have on his account')
    print('-' * 100)
    accounts = []
    create_account(accounts, 1, 'Fred', -500)
    create_account(accounts, 1, 'Bob', 500)
    create_account(accounts, 2, 'Fred', 600)
    deposit(accounts, 1,-100)
    withdraw(accounts, 1, -100)
    transfer(accounts, 1, 2, -100)
    transfer(accounts,1,2,1000)
    transfer(accounts, 2, 1, 900)
    print()


def test_4():
    print('-'*100)
    print('Test 4')
    print('A test to verify the correctness of the all methods,\n'
          'using normal cases')
    print('-' * 100)
    accounts = []
    create_account(accounts, 1, 'Bob', 500)
    create_account(accounts, 2, 'Fred', 600)
    deposit(accounts, 1,100)
    withdraw(accounts, 2, 200)
    transfer(accounts, 1, 2, 400)
    get_balance(accounts,1)
    get_balance(accounts,2)
    print()




