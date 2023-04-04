def create_account(accounts, number, name, amount):
    for data in accounts:
        if data['number'] == number:
            return f'Невозможно открыть счёт с номером счёта {number}'
    if amount < 0:
        return f'Невозможно открыть счёт с начальной суммой {amount}'
    accounts.append({'name': name, 'number': number, 'amount': amount})
    return 'Счёт добавлен'


def deposit(accounts, number, amount):
    if amount <= 0:
        return 'Нельзя зачислить неположительную сумму на счёт'
    for data in accounts:
        if data['number'] == number:
            data['amount'] += amount
            return f'Сумма {amount} успешна зачислена нас счёт {number}'
    return f'Счёта {number} не нашлось'


def withdraw(accounts, number, amount):
    if amount <= 0:
        return 'Нельзя снять неположительную сумму с счёта'
    for data in accounts:
        if data['number'] == number:
            if data['amount'] < amount:
                return 'На счёте недостатоно средств'
            data['amount'] -= amount
            return f'Сумма {amount} успешна снята со счёта {number}'
    return f'Счёта {number} не нашлось'


def transfer(accounts, sender, receiver, amount):
    flag1 = False
    flag2 = False
    i = 0
    while (i < len(accounts)) and (not flag1 or not flag2):
        if accounts[i]['number'] == sender:
            flag1 = True
        if accounts[i]['number'] == receiver:
            flag2 = True
        i += 1
    if (not flag1) and (not flag2):
        return f'Счёта {sender} и {receiver} не нашлись'
    if not flag1:
        return f'Счёта {sender} не нашлось'
    if not flag2:
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
    for data in accounts:
        if data['number'] == number:
            return data['amount']
    return f'Счёта {number} не нашлось'


bank = [{'name': 'Вася', 'number': 12345, 'amount': 1000},
        {'name': 'Петя', 'number': 67890, 'amount': 1000}]

