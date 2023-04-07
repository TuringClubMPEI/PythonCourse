def find_in_accounts(accounts, number):
    res = list(filter(lambda x: x['number'] == number, accounts))
    return res[0] if len(res) > 0 else None


def create_account(accounts, number, name, amount):
    if find_in_accounts(accounts, number):
        return f'Невозможно открыть счёт с номером счёта {number}'
    if amount <= 0:
        return f'Невозможно открыть счёт с начальной суммой {amount}'
    accounts.append({'name': name, 'number': number, 'amount': amount})
    return 'Счёт добавлен'


def deposit(accounts, number, amount):
    data = find_in_accounts(accounts, number)
    if not data:
        return f'Счёта {number} не нашлось'
    if amount <= 0:
        return 'Нельзя зачислить неположительную сумму на счёт'

    data['amount'] += amount
    return f'Сумма {amount} успешна зачислена нас счёт {number}'


def withdraw(accounts, number, amount):
    data = find_in_accounts(accounts, number)
    if not data:
        return f'Счёта {number} не нашлось'
    if amount <= 0:
        return 'Нельзя снять неположительную сумму с счёта'
    if data['amount'] < amount:
        return 'На счёте недостатоно средств'

    data['amount'] -= amount
    return f'Сумма {amount} успешна снята со счёта {number}'


def transfer(accounts, sender, receiver, amount):
    data1 = find_in_accounts(accounts, sender)
    data2 = find_in_accounts(accounts, receiver)
    if (not data1) and (not data2):
        return f'Счёта {sender} и {receiver} не нашлись'
    if not data1:
        return f'Счёта {sender} не нашлось'
    if not data2:
        return f'Счёта {receiver} не нашлось'
    message1 = withdraw(accounts, sender, amount)
    message2 = deposit(accounts, receiver, amount)
    # Проверяем можно ли снять деньги со счёта sender
    if message1 != f'Сумма {amount} успешна снята со счёта {sender}':
        return message1
    # Если нельзя зачислить на счёт receiver, возвращаем деньги на счёт sender
    if message2 != f'Сумма {amount} успешна зачислена нас счёт {receiver}':
        deposit(accounts, sender, amount)
        return message2
    return f'Сумма {amount} успешно переведена со счёта {sender} на счёт {receiver}'


def get_balance(accounts, number):
    data = find_in_accounts(accounts, number)
    if not data:
        return f'Счёта {number} не нашлось'

    return data['amount']


bank = [{'name': 'Вася', 'number': 12345, 'amount': 1000},
        {'name': 'Петя', 'number': 67890, 'amount': 1000}]

#  create_account
#  Такой номер счёта уже есть
print(create_account(bank, 12345, 'Анастасия', 5000))
#  Сумма = 0
print(create_account(bank, 42546, 'Анастасия', 0))
#  Сумма < 0
print(create_account(bank, 42546, 'Анастасия', -100))
#  Можно добавить в банк
print(create_account(bank, 42546, 'Анастасия', 5000))

print()

#  deposit
#  Счёта нет
print(deposit(bank, 163856, 1000))
#  Сумма = 0
print(deposit(bank, 42546, 0))
#  Сумма < 0
print(deposit(bank, 42546, -100))
# Можно зачислить
print(deposit(bank, 42546, 1000))

print()

#  withdraw
#  Счёта нет
print(withdraw(bank, 163856, 1000))
#  Сумма = 0
print(withdraw(bank, 42546, 0))
#  Сумма < 0
print(withdraw(bank, 42546, -100))
#  Сумма больше той, что на счёте
print(withdraw(bank, 42546, 10000))
# Можно снять
print(withdraw(bank, 42546, 500))

print()

#  transfer
# Нет счетов sender и receiver
print(transfer(bank, 275639, 45639, 1000))
#  Счёта sender нет
print(transfer(bank, 163856, 42546, 1000))
#  Счёта receiver нет
print(transfer(bank, 42546, 163856, 1000))
#  Сумма = 0
print(transfer(bank, 42546, 12345, 0))
#  Сумма < 0
print(transfer(bank, 42546, 12345, -100))
#  Сумма больше той, что на счёте
print(transfer(bank, 42546, 12345, 10000))
#  Можно перевести
print(transfer(bank, 42546, 12345, 500))

print()

#  get_balance
#  Счёта нет
print(get_balance(bank, 163856))
# Можно посмотреть баланс
print(get_balance(bank, 42546))
