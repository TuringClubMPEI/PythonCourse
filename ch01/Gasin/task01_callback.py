def fabric(accs, fun):
    def inner(*args):
        return fun(accs, *args)

    return inner


def _find_acc(accounts, number):
    for account in accounts:
        if account.get('number') == number:
            return account


def _create_account(accounts, number, name, amount):
    # Не можем создать счет с балансом меньше нуля
    if amount < 0:
        return
    # Если нашли счет, который имеет тот же номер, ничего не создаем
    if _find_acc(accounts, number) is not None:
        return
    new_acc = {'number': number, 'name': name, 'amount': amount}
    accounts.append(new_acc)
    return new_acc


def _deposit(accounts, number, amount):
    # Не можем пополнить счет на отрицательное число или 0
    if amount <= 0:
        return
    acc = _find_acc(accounts, number)
    # Если не нашли аккаунт, ничего не делаем
    if acc is None:
        return
    acc['amount'] += amount
    return acc


def _withdraw(accounts, number, amount):
    # Не можем снять отрицательную сумму денег или 0
    if amount <= 0:
        return
    acc = _find_acc(accounts, number)
    # Если не нашли счет, снимать не с чего
    if acc is None:
        return
    # Не можем снять больше, чем осталось на счету
    if acc.get('amount') < amount:
        return
    acc['amount'] -= amount
    return acc


def _transfer(accounts, sender, receiver, amount):
    # Не можем перевести меньше или равно нуля денег
    if amount <= 0:
        return
    acc_from = _find_acc(accounts, sender)
    acc_to = _find_acc(accounts, receiver)
    # Если не нашли один из счетов, перевод невозможен
    if acc_to is None or acc_from is None:
        return
    # Если сумма денег на отправителе меньше суммы перевода, перевод невозможен
    if acc_from.get('amount') < amount:
        return
    acc_from['amount'] -= amount
    acc_to['amount'] += amount


def _get_balance(accounts, number):
    acc = _find_acc(accounts, number)
    if acc is not None:
        return acc['amount']


if __name__ == '__main__':
    bank_accounts = []

    create_account = fabric(bank_accounts, _create_account)
    get_balance = fabric(bank_accounts, _get_balance)
    deposit = fabric(bank_accounts, _deposit)
    withdraw = fabric(bank_accounts, _withdraw)
    transfer = fabric(bank_accounts, _transfer)

    print('Создание счетов')
    create_account(1, 'Misha', 1000)
    create_account(2, 'Pasha', 1000)
    print(bank_accounts)
    print()

    print('Проверка баланса')
    print(get_balance(1))  # 1000
    print(get_balance(0))  # None
    print()

    print('Депозит')
    # Положим сумму на несуществующий счет
    deposit(-1, 1000)
    print(bank_accounts)
    # Положим сумму меньше нуля
    deposit(1, -2)
    print(get_balance(1))  # 1000
    # Положим правильную сумму
    deposit(1, 1000)
    print(get_balance(1))  # 2000
    print()

    print('Снятие денег')
    # Снимем деньги с несуществующего счета
    withdraw(-1, 10)
    print(bank_accounts)
    # Снимем сумму меньше нуля
    withdraw(1, -500)
    print(get_balance(1))  # 2000
    # Снимем сумму больше, чем на счету
    withdraw(1, 5000)
    print(get_balance(1))  # 2000
    # Снимем корректную сумму
    withdraw(1, 500)
    print(get_balance(1))  # 1500
    print()

    print('Перевод денег со счета на счет')
    # Переводим меньше нуля денег
    transfer(1, 2, -500)
    print(bank_accounts)
    # Отправитель не найден
    transfer(-1, 2, 500)
    print(bank_accounts)
    # Получатель не найден
    transfer(1, -2, 500)
    print(bank_accounts)
    # Переводим сумму больше, чем есть на счете
    transfer(1, 2, 3000)
    print(bank_accounts)
    # Переводим правильную сумму
    transfer(1, 2, 500)
    print(bank_accounts)