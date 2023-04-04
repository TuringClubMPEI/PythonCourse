
def find_by_key(iterable, key, value):
#функция поиска словаря в списке
    for index, dict_ in enumerate(iterable):
        if key in dict_ and dict_[key] == value:
            return (dict_)

def create_account(account, number, name, amount):
#функция для создания нового счета.
    dict = {"account" : account, "number" : number, "name" : name, "amount" : amount}
    dict1 = find_by_key(list_of_clients, "number", number)
    # print(dict1)
    if dict1!=None:
        print("error: номер занят")
    elif float(dict["amount"])<0:
        print("error: нельзя вводить отрицательные суммы")
    else:
        list_of_clients.append(dict)

def deposit(account, number, amount):
# функция для пополнения счета.
    dict = find_by_key(list_of_clients, "number", number)

    if float(dict["amount"]) < 0:
        print("error: нельзя вводить отрицательные суммы")
    else:
        dict["amount"] = str(float(dict["amount"]) + float(amount))


def withdraw(account, number, amount):
# функция для снятия денег со счета
    dict = find_by_key(list_of_clients, "number", number)
    if dict["amount"] < amount:
        print("error: на счете недостаточно средств")
    else:
        dict["amount"] = str(float(dict["amount"]) - float(amount))

def transfer(account, sender, receiver, amount):
#  функция для перевода средств между счетами.
    dict_sender = find_by_key(list_of_clients, "number", sender)
    if dict_sender["amount"] < amount:
        print(f'error: на счете sender недостаточно средств')
    else:
        dict_sender["amount"] = str(float(dict_sender["amount"]) - float(amount))
        dict_receiver = find_by_key(list_of_clients, "number", receiver)
        dict_receiver["amount"] = str(float(dict_sender["amount"]) + float(amount))


def get_balance(account, number):
# функция для получения текущего баланса.
    dict = find_by_key(list_of_clients, "number", number)
    print("name = ", dict["name"], "amount =", dict["amount"])

if __name__ == '__main__':
    global list_of_client
    list_of_clients = []
    # create_account()
    i = 0
    s = input("1 (start) or 0 (stop)")
    while (s == '1'):
        answer = input("choose:\n"
                       "1 = create account \n"
                       "2 = deposit \n"
                       "3 = withdraw \n"
                       "4 = transfer \n"
                       "5 = get balance")
        if answer == '1': #создание нового счета.
            account = input("write accounts")
            number = input("write number")
            name = input("write name")
            amount = input("write client's amount")
            create_account(account, number, name, amount)

        if answer == '2': #пополнение счета
            account = input("write accounts")
            number = input("write number")
            amount = input("write client's amount")
            deposit(account, number, amount)

        if answer == '3': #снятие денег со счета
            account = input("write accounts")
            number = input("write number")
            amount = input("write client's amount")
            withdraw(account, number, amount)

        if answer == '4': #перевод средств между счетами.
            account = input("write accounts")
            sender = input("write number of sender")
            receiver = input("write number of receiver")
            amount = input("write client's amount")
            transfer(account, sender, receiver, amount)

        if answer == '5': #получение текущего баланса
            account = input("write accounts")
            number = input("write client's number ")
            get_balance(account, number)

        print(list_of_clients)


        s = input("1 (continue) or 0 (stop)")






