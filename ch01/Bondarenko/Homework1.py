# создание счёта
def create_account(accounts, number, name, amount):
    new_account = {"number_of_account": number, "name_of_account": name, "amount_of_account": amount}
    accounts.append(new_account)
    return 0

# пополнение счёта
def deposit(accounts, number, amount):
    for i in range(len(accounts)):
        value_number = accounts[i].get("number_of_account", None)
        if (number == value_number):
            accounts[i]["amount_of_account"] += amount
            break
    return 0

# снятие средств со счёта
def withdraw(accounts, number, amount):
    for i in range(len(accounts)):
        value_number = accounts[i].get("number_of_account", None)
        if (number == value_number):
            accounts[i]["amount_of_account"] -= amount
            break
    return 0

# перевод между счетами
def transfer(accounts, sender, receiver, amount):
    withdraw(accounts, sender, amount)
    deposit(accounts, receiver, amount)
    return 0

# информация о счёте
def get_balance(accounts, number):
    for i in range(len(accounts)):
        value_number = accounts[i].get("number_of_account", None)
        if (number == value_number):
            print("На счете", accounts[i]["name_of_account"] , "находится", accounts[i]["amount_of_account"], "у.е.")
            break
    return 0

# проверка, существует ли введённый номер счёта
def checking_account(accounts, number):
    flag = False
    number_of_cycles = 0
    for i in range(len(accounts)):
        value_of_number = accounts[i].get("number_of_account", None)
        if (number == value_of_number):
            flag = True
    while (flag == False) and (number_of_cycles == 0): # если такого счёта нет, пытаемся ещё раз ввести (6 попыток)
        for attempts in range(1, 8):
            if (7 - attempts != 0):
                print("Ошибка операции. Введён несуществующий номер счёта. Проверьте номер введённого Вами номера счёта и повторите ввод. У вас осталось", 7 - attempts, "попыток ввода.")
                number = int(input())
                if (number == value_of_number):
                    flag == True
                    break
            else:
                print("Попытки закончились. Операция завершена:(")
                number_of_cycles = 1
    return flag

# проверка возможности снятия указанной суммы с аккаунта
def checking_amount_of_withdraw(accounts, number):
    for i in range(len(accounts)):
        value_number = accounts[i].get("number_of_account", None)
        if (number == value_number):
            podh_account = i
            amount_of_account = bank[podh_account]["amount_of_account"]
    print("Введите сумму.")
    amount = int(input())
    while (amount > amount_of_account) or (amount < 0):
        print("Введено некорректное значение суммы")
        amount = int(input())
    return amount


bank = [] #пустой список для хранения словарей-данных о счетах
stop_signal = True #сигнал, позволяющий прекратить или продолжить выполнение операций со счетами

while (stop_signal == True):
    print("Выберите, какую операцию вы хотите произвести:")
    print(" 1 - Создать новый счёт;\n", "2 - Пополнить счёт;\n", "3 - Снять деньги со счёта;\n", "4 - Выполнить перевод средств с одного счёта на другой;\n", "5 - Узнать количество средств, оставшихся на счёте.\n")
    operation_number = int(input())

#в зависимости от введённого кода выполняем одну из операций
    if (0 < operation_number < 6):
        match operation_number:

            case 1: #создание счёта
                creating_flag = True
                while(creating_flag == True):
                    creating_flag = False
                    print("Введите номер создаваемого счёта")
                    creating_number = int(input())
                    for i in range(len(bank)):
                        value_of_number = bank[i].get("number_of_account", None)
                        if (creating_number == value_of_number):
                            print("Такой номер счёта уже существует. Повторите ввод номера.")
                            creating_flag = True
                print("Введите ФИО владельца создаваемого счёта")
                creating_name = input()
                creating_amount = -1
                while (creating_amount < 0):
                    print("Введите начальную сумму, которая будет храниться на счёте")
                    creating_amount = int(input())
                    if (creating_amount < 0):
                        print("Введено отрицательное значение начальной суммы. Продолжение операции невозможно. Повторите ввод.")
                create_account(bank, creating_number, creating_name, creating_amount)

            case 2: #пополнение счёта
                print("Введите номер счёта пополнения.")
                deposit_number = int(input())
                deposit_flag = checking_account(bank, deposit_number)
                if(deposit_flag == True):
                    deposit_amount = -1
                    while (deposit_amount <= 0):
                        print("Введите сумму пополнения.")
                        deposit_amount = int(input())
                        if (deposit_amount <= 0):
                            print("Введено некорректное значение суммы пополнения. Продолжение операции невозможно. Повторите ввод.")
                    deposit(bank, deposit_number, deposit_amount)
                    print("Вы успешно пополнили счёт.")

            case 3: #снятие средств со счёта
                print("Введите номер счёта снятия.")
                withdraw_number = int(input())
                withdraw_flag = checking_account(bank, withdraw_number)
                podh_account = 1
                if(withdraw_flag == True):
                    withdraw_amount = checking_amount_of_withdraw(bank, withdraw_number)
                    withdraw(bank, withdraw_number, withdraw_amount)
                    print("Снятие успешно завершено.")

            case 4: #перевод между счетами
                print("Введите номер счёта, с которого будет осуществлён перевод")
                sender_number = int(input())
                sender_flag = checking_account(bank, sender_number)
                if(sender_flag == True):
                    print("Введите номер счёта, куда будет осуществлён перевод")
                    receive_number = int(input())
                    receive_flag = checking_account(bank,receive_number)
                    if (receive_flag == True):
                        amount_of_transfer = checking_amount_of_withdraw(bank, sender_number)
                        transfer(bank,sender_number, receive_number, amount_of_transfer)
                        print("Перевод успешно осуществлён.")

            case 5: #просмотр информации о счёте
                print("Введите номер счёта просмотра.")
                gb_number = int(input())
                gb_flag = checking_account(bank, gb_number)
                get_balance(bank, gb_number)

    else:
        print("Введён неизвестный код операции")
    print("Хотите ли Вы продолжить (y or n)?")
    stop_message = input()
    if (stop_message.lower() != "y"):
        stop_signal = False







