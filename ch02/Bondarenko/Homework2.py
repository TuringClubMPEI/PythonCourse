class Account:   #cоздаём класс Account c геттерами и сеттерами на сумму и номер аккаунта.
    def __init__(self, number: int, name: str, amount: int):
        self.__number = number
        self.__name = name
        self.__amount = amount

    def checking_amount(func): #декоратор проверки суммы на отрицательность
        def wrapper (self, *args):
            if (args[-1] < 0):
                print("Сумма должна быть больше или равна нулю.")
                return
            func(self, *args)
        return wrapper

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, addAmount):
        self.__amount = addAmount

    @property
    def number(self):
        return self.__number

    @checking_amount
    def deposit(self, amount):
        self.__amount += amount


    @checking_amount
    def withdraw(self, amount):
        if (self.__amount < amount):
            print("На счёте недостаточно средств.")
            return
        self.__amount -= amount

class Bank:
    def __init__(self):
        self.__accounts = []


    def checking_amount(func): #декоратор проверки суммы на отрицательность
        def wrapper (self, *args):
            if args[-1] < 0:
                print("Сумма должна быть больше или равна нулю.")
                return
            func(self, *args)
        return wrapper

    def finding_account(self, number): #поиск счёта с подходящим номером
        find = list(filter(lambda x: x.number == number, self.__accounts))
        return find[0] if (len(find) > 0) else None



    def checking_account(func): #декоратор проверки счёта на существование
        def wrapper (self, *args):
            account = self.finding_account(args[0])
            if account is None:
                print("Счёта с номером", args[0], "не существует.")
                return
            func(self, account, *args[1:])
        return wrapper

    @checking_amount
    def create_account(self, number, name, amount):
        if self.finding_account(number) is not None:
            print("Счёт с номером", number, "уже существует.")
            return
        if (number < 1):
            print("Номер создаваемого счёта должен быть положительным числом.")
            return
        self.__accounts.append((Account(number, name, amount)))


    @checking_account
    @checking_amount
    def deposit(self, account, d_amount):
        account.deposit(d_amount)

    @checking_account
    @checking_amount
    def withdraw(self, account, w_amount):
        account.withdraw(w_amount)

    @checking_amount
    def transfer(self, sender, receiver, t_amount):
        sender_acc = self.finding_account(sender)
        if sender_acc is None:
            print("Счёта с номером", sender, "не существует.")
            return
        receiver_acc = self.finding_account(receiver)
        if sender_acc is None:
            print("Счёта с номером", sender, "не существует.")
            return
        if sender_acc.amount < t_amount:
            print("На счёте отправителя недостаточно средств для осуществления операции.")
            return
        sender_acc.amount -= t_amount
        receiver_acc.amount += t_amount

    @checking_account
    def get_balance(self, account):
        print("На счёте под номером", account.number, "хранится", account.amount, "у.е.")


stop_signal = True #сигнал, позволяющий прекратить или продолжить выполнение операций со счетами
bank = Bank()
while (stop_signal == True):
    print("Выберите, какую операцию вы хотите произвести:")
    print(" 1 - Создать новый счёт;\n", "2 - Пополнить счёт;\n", "3 - Снять деньги со счёта;\n", "4 - Выполнить перевод средств с одного счёта на другой;\n", "5 - Узнать количество средств, оставшихся на счёте.\n")
    operation_number = int(input())

#в зависимости от введённого кода выполняем одну из операций
    if (0 < operation_number < 6):
        match operation_number:

            case 1: #создание счёта
                print("Введите номер создаваемого аккаунта")
                creating_number = int(input())
                print("Введите ФИО владельца создаваемого счёта")
                creating_name = input()
                print("Введите сумму, которая изначально будет хранится на счёте")
                creating_amount = int(input())
                bank.create_account(creating_number, creating_name, creating_amount)
                print("Выполнение операции завершено.")

            case 2: #пополнение счёта
                print("Введите номер счёта пополнения.")
                deposit_number = int(input())
                print("Введите сумму пополнения.")
                deposit_amount = int(input())
                bank.deposit(deposit_number, deposit_amount)
                print("Выполнение операции завершено.")

            case 3: #снятие средств со счёта
                print("Введите номер счёта снятия.")
                withdraw_number = int(input())
                print("Введите сумму снятия")
                withdraw_amount = int(input())
                bank.withdraw(withdraw_number, withdraw_amount)
                print("Выполнение операции завершено.")

            case 4: #перевод между счетами
                print("Введите номер счёта, с которого будет осуществлён перевод")
                sender_number = int(input())
                print("Введите номер счёта, куда будет осуществлён перевод")
                receive_number = int(input())
                print("Введите сумму перевода.")
                transfer_amount = int(input())
                bank.transfer(sender_number, receive_number, transfer_amount)
                print("Выполнение операции завершено.")


            case 5: #просмотр информации о счёте
                print("Введите номер счёта просмотра.")
                gb_number = int(input())
                bank.get_balance(gb_number)
                print("Выполнение операции завершено.")

    else:
        print("Введён неизвестный код операции")
    print("Хотите ли Вы продолжить (y or n)?")
    stop_message = input()
    if (stop_message.lower() != "y"):
        stop_signal = False
