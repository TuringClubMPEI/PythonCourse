from decorators import *
class Account:

    @number_checker
    def __init__(self, number : int, name : str,  balance : int):
        self.__number = number
        self.__name = name
        self.__balance = balance
        print('Аккаунт успешно создан')
        bank.accounts.append(self)

    @staticmethod
    def account_exists(number) -> bool:
        return len(list(filter(lambda x: x.number == number, bank.accounts))) != 0

    @property
    def number(self):
        return self.__number

    @property
    def name(self):
        return self.__name

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @deposit_validation
    def deposit(self,amount):
        self.__balance+=amount
        print('счет успешно пополнен')

    @withdraw_validation
    def withdraw(self,amount):
        self.__balance-=amount
        print('Снятие средств прошло успешно')

    def getbalance(self):
        print(self.__number,self.__name,self.__balance)


class Bank:

    def __init__(self):
        self.__accounts = []

    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, value):
        self.__accounts = value

    @transfer_validation
    def transfer(self, sender : Account, receiver: Account, amount : int):
        sender.balance -= amount
        receiver.balance += amount
        print ('Перевод выполнен успешно')

    #def robbery(self):
        #self.__accounts = list(map(lambda x: x.balance * 0, self.__accounts))
        #print('Все ваши деньги украдены хе хе')
        #Паша, помоги плиз, я хотела сделать эту функция по приколу,а по итогу оно не работает и
        #создает другой массив в у которого все атрибуты=0, не только баланс


bank=Bank()
Gasin=Account(1,'Misha',1000)
Zhukov=Account(2,'Pasha',1000)
Fofanov=Account(3,'Sasha',1000)
Kobzev=Account(3,'Sasha',1000)
Kobzev=Account(4,'Sasha',1000)
Gordov=Account(5,'Sasha',-6)
Gordov=Account(5,'Sasha',1000)

#Нормальные значения
Fofanov.getbalance()
Gasin.deposit(500)
Gasin.getbalance()
bank.transfer(Kobzev,Zhukov,700)
Kobzev.getbalance()
Zhukov.getbalance()

#ошибки
Fofanov.withdraw(5000)
bank.transfer(Gordov,Gasin,-6)
bank.transfer(Gordov,Gasin,10000)





















