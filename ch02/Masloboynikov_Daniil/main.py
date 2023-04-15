
class Bank:
    list_of_clients = []
    def __init__(self):
        print("создаем список клиентов")
    def set_list(self, Check):
        self.list_of_clients.append(Check)
        print("Добовляем клиента")
    def find_number(self, number):
        for list in self.list_of_clients:
            if list.number == number:
                return(list)

    def transfer(self, sender, receiver, amount):
        self = self.find_number(sender)
        self._amount = float(self.amount) - float(amount)
        self = self.find_number(receiver)
        self._amount = float(self.amount) + float(amount)

class Check(Bank):
    def __init__(self, number = 123, name = "asd", amount = 0.0):
        self._number = number
        self._name = name
        self._amount = amount

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
        self = bank.find_number(number)
        self._amount = float(self.amount) + float(amount)

    def withraw(self, number, amount):
        # функция для пополнения счета.
        self = bank.find_number(number)
        self._amount = float(self.amount) - float(amount)

    def get_balance(self, number):
    # функция для получения текущего баланса.
        self = bank.find_number(number)
        print(self.amount)


if __name__ == '__main__':
    list_of_clients = []
    bank = Bank()
    # # create_account()
    i = 0
    list = []
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
            check = Check()
            check.deposit(number, amount)

        if answer == '3': #снятие денег со счета
            number = input("write number")
            amount = input("write client's amount")
            check = Check()
            check.withraw(number, amount)

        if answer == '4': #перевод средств между счетами.
            sender = input("write number of sender")
            receiver = input("write number of receiver")
            amount = input("write client's amount")
            bank.transfer(sender, receiver, amount)
    #
        if answer == '5': #получение текущего баланса
            number = input("write client's number ")
            check = Check()
            check.get_balance(number)

        for list in bank.list_of_clients:
            print( "number = ", list.number, "amount = ", list.amount, '\n')

        s = input("1 (continue) or 0 (stop)")






