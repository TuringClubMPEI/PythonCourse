
class Bank:
    list_of_clients = []
    def __init__(self):
        print("создаем список клиентов")
    def set_list(self, сheck):
        self.list_of_clients.append(сheck)
        print("Добовляем клиента")
    def find_number(self, number):
        for list in self.list_of_clients:
            if list.number == number:
                return(list)

    def transfer(self, sender, receiver, amount):
        self_sender = self.find_number(sender)
        if self.find_number(sender) == None:
            print("пользователя <отправиитель> не существует")
        elif float(self_sender._amount) - float(amount) < 0:
            print("сумма превышает остаток на счете")
        elif self.find_number(receiver) == None:
            print("пользователя <получатель> не существует")
        else:
            self_sender._amount = float(self_sender.amount) - float(amount)
            self_receiver = self.find_number(receiver)
            self_receiver._amount = float(self_receiver.amount) + float(amount)

class Check(Bank):
    def __init__(self, number = 123, name = "asd", amount = 0.0):
        self._number = number
        self._name = name
        self._amount = amount
        if self.find_number(number)!=None:
            raise Exception ("Пользователь с данным номером уже существует")



    def __del__(self):
        pass
    def get_amount(self):
        return self._amount

    def set_amount(self, x = 0.0):
        self._amount = float(self._amount) + float(x)

    amount = property(get_amount, set_amount)

    def get_number(self):
        return self._number

    def set_number(self, x):
        self._number = x

    number = property(get_number, set_number)

    def deposit(self, number, amount):
        # функция для пополнения счета.
        self_number = bank.find_number(number)
        self_number._amount = float(self_number.amount) + float(amount)

    def withraw(self, number, amount):
        # функция для пополнения счета.
        self_number = bank.find_number(number)
        if float(self_number.amount) - float(amount) < 0:
            print("превышает остаток средств")
        else:
            self_number._amount = float(self_number.amount) - float(amount)


    def get_balance(self, number):
    # функция для получения текущего баланса.
        self_number = bank.find_number(number)
        return self_number.amount

if __name__ == '__main__':
    bank = Bank()
    check = Check()

    s = input("1 (start) or 0 (stop)")
    while (s == '1'):
        answer = input("choose:\n"
                       "1 = create account \n"
                       "2 = deposit \n"
                       "3 = withdraw \n"
                       "4 = transfer \n"
                       "5 = get balance")
        if answer == '1': #создание нового счета.
            number = input("write number")
            name = input("write name")
            amount = input("write client's amount")
            bank.set_list(Check(number, name, amount))


        if answer == '2': #пополнение счета
            number = input("write number")
            amount = input("write client's amount")
            check.deposit(number, amount)

        if answer == '3': #снятие денег со счета
            number = input("write number")
            amount = input("write client's amount")
            check.withraw(number, amount)

        if answer == '4': #перевод средств между счетами.
            sender = input("write number of sender")
            receiver = input("write number of receiver")
            amount = input("write client's amount")
            bank.transfer(sender, receiver, amount)
    #
        if answer == '5': #получение текущего баланса
            number = input("write client's number ")
            print(check.get_balance(number))


        for list in bank.list_of_clients:
            print( "number = ", list.number, "; amount = ", list.amount)

        s = input("1 (continue) or 0 (stop)")






