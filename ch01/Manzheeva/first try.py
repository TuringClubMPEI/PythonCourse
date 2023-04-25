def searching_for_account(accounts, number):
    for user in accounts:
        if user['number'] == number:
            return user

def create_account(accounts, number, name, amount):
    if amount < 0:
        print("\nОшибка, баланс не может быть отрицательным\n")
        return
    for user in accounts:
        if user.get('number') == number:
            print("\nТакой номер уже существует\n")
            return
    new_account = {'number': number, 'name': name, 'amount': amount}
    accounts.append(new_account)
    print("\nАккаунт успешно создан\n")
    return


def deposit(accounts, number, amount):  #
    if amount < 0:
        print("\nОшибка, пополнение не может быть отрицательным\n")
        return
    user = searching_for_account(accounts, number)
    if user is None:
        print("\n Ошибка, такого аккакунта не найдено\n")
        return
    print("\nСчет до пополнения")
    print(user)
    user['amount'] = user['amount'] + amount
    print('\nСчет после пополнения')
    print(user)
    return


def withdraw(accounts, number, amount):
    if amount < 0:
        print("\nОшибка, сумма снятия не может быть отрицательной\n")
        return
    user = searching_for_account(accounts, number)
    if user is None:
        print("\n Ошибка, такого аккакунта не найдено\n")
        return
    if amount > user['amount']:
        print("\n Ошибка, вы не можете снять сумму больше имеющейся на счете\n")
        return
    print("\nСчет до снятия")
    print(user)
    user['amount'] = user['amount'] - amount
    print('\nСчет после снятия')
    print(user)
    return


def transfer(accounts, sender, receiver, amount):
    if amount < 0:
        print("\nОшибка, сумма перевода не может быть отрицательной\n")
        return
    user1 = searching_for_account(accounts, sender)
    if user1 is None:
        print("\n Ошибка, такого аккакунта отправителя не найдено\n")
        return
    if amount > user1['amount']:
        print("\n Ошибка, вы не можете перевести сумму больше имеющейся на счете\n")
        return
    user2 = searching_for_account(accounts, receiver)
    if user2 is None:
        print("\n Ошибка, такого аккакунта получателя не найдено\n")
        return
    print("\nСчета до перевода")
    print(user1)
    print(user2)
    user1['amount'] = user1['amount'] - amount
    user2['amount'] = user2['amount'] + amount
    print('\nСчета после перевода')
    print(user1)
    print(user2)
    return


def get_balance(accounts, number):
    user = searching_for_account(accounts, number)
    if user is None:
        print("\n Ошибка, такого аккакунта не найдено\n")
        return
    print(user)
    return


if __name__ == '__main__':

    list_of_acc = []

    while True:
        a = input(
            "\nДля создание аккаунта нажмите 1\nДля пополнения счета нажмите 2\nДля снятия денег со счета нажмите 3\nДля переводча между счетами нажите 4\nДля получения текущего баланса нажмите 5\nДля завершения программы нажмите 0\n")

        if (int(a) < 0 or int(a) > 5):
            print("Некорректный ввод\n")
            continue

        if a == '1':
            usr_number = input("Введите номер счета ")
            usr_name = input("Введите имя владльца ")
            usr_amount = int(input("Введите начальный баланс "))
            create_account(list_of_acc, usr_number, usr_name, usr_amount)

        if a == '2':
            usr_number = input("Введите номер счета ")
            usr_amount = int(input("Ввидите сумму пополнения "))
            deposit(list_of_acc, usr_number, usr_amount)

        if a == '3':
            usr_number = input("Введите номер счета ")
            usr_amount = int(input("Ввидите сумму списания "))
            withdraw(list_of_acc, usr_number, usr_amount)

        if a == '4':
            usr_sender = input("Введите номер счета отправителя ")
            usr_receiver = input("Введите номер плучателя отправителя ")
            usr_amount = int(input("Ввидите сумму перевода "))
            transfer(list_of_acc, usr_sender, usr_receiver, usr_amount)

        if a == '5':
            usr_number = input("Введите номер счета")
            get_balance(list_of_acc, usr_number)

        if a == '0':
            break

