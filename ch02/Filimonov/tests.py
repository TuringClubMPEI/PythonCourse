from SecondTask import *

bank = Bank()
bank.create_account(-1, 'jkfdbk', 5)
bank.create_account(1, 'jkfdbk', -5)
bank.create_account(1, 'jkfdbk', 5)
bank.create_account(1, 'jkfdbk', 5984303)

bank.create_account(23, 'jkfdbk', 40)

bank.deposit(2, 10)
bank.deposit(1, -12)
bank.deposit(1, 10)

bank.withdraw(2, 10)
bank.withdraw(1, -10)
bank.withdraw(1, 100)
bank.withdraw(1, 10)

bank.transfer(-23, 1, 30)
bank.transfer(23, -2, 30)
bank.transfer(23, 1, -30)
bank.transfer(23, 1, 30000)
bank.transfer(23, 1, 30)

bank.get_balance(2)
bank.get_balance(1)
bank.get_balance(23)